# plugins/command_loader.py
"""
This module provides help functionalities for the application.
"""
import importlib.util
import os
from plugins.command_handler import Command

class CommandLoader:
    """
    Command class represents a generic command.
    """
    def __init__(self, plugin_directory, command_handler):
        """Execute the command."""
        self.plugin_directory = plugin_directory
        self.command_handler = command_handler

    def load_plugins(self):
        """Execute the command."""
        for filename in os.listdir(self.plugin_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module_path = os.path.join(self.plugin_directory, filename)
                self._load_plugin(module_name, module_path)

    def _load_plugin(self, module_name, module_path):
        """Execute the command."""
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                init_method = getattr(attribute, '__init__', None)
                if callable(init_method) and hasattr(init_method, '__code__'):
                    if 'command_handler' in init_method.__code__.co_varnames:
                        command_instance = attribute(self.command_handler)
                    else:
                        command_instance = attribute()
                else:
                    command_instance = attribute()
                self.command_handler.register_command(module_name, command_instance)
