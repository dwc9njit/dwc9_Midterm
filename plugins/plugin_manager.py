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
                if self._is_valid_plugin_file(filename):
                    module_name = filename[:-3]
                    self.logger.info("Loading module: %s", module_name)
                    self._load_module_plugins(module_name)
        except (ImportError, AttributeError, TypeError) as e:
            self.logger.error("Error loading plugins: %s", e)

    def _is_valid_plugin_file(self, filename):
        """
        Check if a file is a valid plugin file.
        
        Args:
            filename (str): The name of the file to check.
        
        Returns:
            bool: True if the file is a valid plugin file, False otherwise.
        """
        return filename.endswith(".py") and filename != "__init__.py"

    def _load_module_plugins(self, module_name):
        """
        Load plugins from a module.
        
        Args:
            module_name (str): The name of the module to load plugins from.
        """
        module = importlib.import_module(f"plugins.{module_name}")
        for attr in dir(module):
            cls = getattr(module, attr)
            if self._is_valid_plugin_class(cls):
                instance = self._create_plugin_instance(cls)
                command_name = instance.get_command_name()
                self.plugins[command_name] = instance
                self.logger.info("Plugin loaded: %s", command_name)

    def _is_valid_plugin_class(self, cls):
        """
        Check if a class is a valid plugin class.
        
        Args:
            cls (type): The class to check.
        
        Returns:
            bool: True if the class is a valid plugin class, False otherwise.
        """
        return isinstance(cls, type) and issubclass(cls, CommandPlugin) and cls is not CommandPlugin

    def _create_plugin_instance(self, cls):
        """
        Create an instance of a plugin class.
        
        Args:
            cls (type): The plugin class to create an instance of.
        
        Returns:
            CommandPlugin: An instance of the plugin class.
        """
        if cls.__name__ == "HelpCommand" and self.command_handler:
            return cls(command_handler=self.command_handler)
        return cls()

    def get_plugin(self, name):
        """
        Retrieve a plugin by its command name.
        
        Args:
            name (str): The command name of the plugin to retrieve.
        
        Returns:
            CommandPlugin: The plugin instance associated with the given command name.
        """
        return self.plugins.get(name)
