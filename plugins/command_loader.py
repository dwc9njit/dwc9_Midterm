# plugins/command_loader.py
import importlib.util
import os
from plugins.command_handler import CommandHandler, Command

class CommandLoader:
    def __init__(self, plugin_folder):
        self.plugin_folder = plugin_folder
        self.command_handler = CommandHandler()
        self.commands = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module_path = os.path.join(self.plugin_folder, filename)
                self._load_plugin(module_name, module_path)

    def _load_plugin(self, module_name, module_path):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                self.commands[module_name] = attribute()

    def get_command(self, name):
        return self.commands.get(name)
