"""
This module manages the loading and retrieval of plugins.
"""

import os
import importlib
import logging
from plugins.plugin_interface import CommandPlugin

class PluginManager:
    """Manages the loading and retrieval of command plugins."""

    def __init__(self, plugin_folder: str, command_handler=None):
        """
        Initialize the PluginManager.
        
        Args:
            plugin_folder (str): The folder where plugin modules are located.
            command_handler: Optional; the command handler to pass to certain plugins.
        """
        self.plugin_folder = plugin_folder
        self.plugins = {}
        self.command_handler = command_handler
        self.logger = logging.getLogger(__name__)
        self.load_plugins()

    def load_plugins(self):
        """
        Load plugins from the specified plugin folder.
        """
        try:
            for filename in os.listdir(self.plugin_folder):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = filename[:-3]
                    self.logger.info("Loading module: %s", module_name)
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
                            self.logger.info("Plugin loaded: %s", command_name)
        except (ImportError, AttributeError, TypeError) as e:
            self.logger.error("Error loading plugins: %s", e)

    def get_plugin(self, name):
        """
        Retrieve a plugin by its command name.
        
        Args:
            name (str): The command name of the plugin to retrieve.
        
        Returns:
            CommandPlugin: The plugin instance associated with the given command name.
        """
        return self.plugins.get(name)
