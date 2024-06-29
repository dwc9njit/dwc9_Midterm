# plugin_manager.py
import os
import importlib
import logging
from plugins.plugin_interface import CommandPlugin

class PluginManager:
    def __init__(self, plugin_folder: str, command_handler=None):
        self.plugin_folder = plugin_folder
        self.plugins = {}
        self.command_handler = command_handler
        self.logger = logging.getLogger(__name__)
        self.load_plugins()

    def load_plugins(self):
        try:
            for filename in os.listdir(self.plugin_folder):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = filename[:-3]
                    self.logger.info(f"Loading module: {module_name}")
                    module = importlib.import_module(f"plugins.{module_name}")
                    for attr in dir(module):
                        cls = getattr(module, attr)
                        if isinstance(cls, type) and issubclass(cls, CommandPlugin) and cls is not CommandPlugin:
                            if cls.__name__ == "HelpCommand" and self.command_handler:
                                instance = cls(command_handler=self.command_handler)
                            else:
                                instance = cls()
                            command_name = instance.get_command_name()
                            self.plugins[command_name] = instance
                            self.logger.info(f"Plugin loaded: {command_name}")
        except Exception as e:
            self.logger.error(f"Error loading plugins: {e}")

    def get_plugin(self, name):
        return self.plugins.get(name)

