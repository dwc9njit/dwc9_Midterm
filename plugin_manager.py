"""
This module manages the loading and retrieval of command plugins.
"""

import os
import importlib
import logging
from plugins.plugin_interface import CommandPlugin

class PluginManager:
    """
    Manages the loading and retrieval of command plugins.

    Attributes:
        plugin_folders (list): List of folders to search for plugins.
        plugins (dict): Dictionary to store loaded plugins.
        logger (logging.Logger): Logger for this class.
    """

    def __init__(self, plugin_folders):
        """
        Initialize the PluginManager with specified plugin folders.

        Args:
            plugin_folders (list): List of folders to search for plugins.
        """
        self.plugin_folders = plugin_folders
        self.plugins = {}
        self.logger = logging.getLogger(__name__)
        self.load_plugins()

    def load_plugins(self):
        """
        Load plugins from the specified plugin folders.
        """
        for folder in self.plugin_folders:
            if not os.path.exists(folder):
                self.logger.error("Plugin folder not found: %s", folder)
                continue
            try:
                for filename in os.listdir(folder):
                    if self._is_valid_plugin_file(filename):
                        module_name = filename[:-3]
                        self.logger.info("Loading module: %s", module_name)
                        self._load_module_plugins(module_name, folder)
            except (ImportError, AttributeError, TypeError) as e:
                self.logger.error("Error loading plugins from %s: %s", folder, e)

    def _is_valid_plugin_file(self, filename):
        """
        Check if a file is a valid plugin file.

        Args:
            filename (str): The name of the file to check.

        Returns:
            bool: True if the file is a valid plugin file, False otherwise.
        """
        return filename.endswith(".py") and filename != "__init__.py"

    def _load_module_plugins(self, module_name, folder):
        """
        Load plugins from a module.

        Args:
            module_name (str): The name of the module to load.
            folder (str): The folder where the module is located.
        """
        try:
            module = importlib.import_module(f"{folder}.{module_name}")
            for attr in dir(module):
                cls = getattr(module, attr)
                if self._is_valid_plugin_class(cls):
                    instance = self._create_plugin_instance(cls)
                    command_name = instance.get_command_name()
                    self.plugins[command_name] = instance
                    self.logger.info("Plugin loaded: %s", command_name)
        except Exception as e:
            self.logger.error("Error loading module %s: %s", module_name, e)

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
            cls (type): The plugin class to instantiate.

        Returns:
            CommandPlugin: An instance of the plugin class.
        """
        self.logger.debug("Creating instance of plugin class: %s", cls.__name__)
        return cls(self)

    def get_plugin(self, name):
        """
        Retrieve a plugin by its command name.

        Args:
            name (str): The command name of the plugin.

        Returns:
            CommandPlugin: The plugin instance, or None if not found.
        """
        self.logger.debug("Retrieving plugin with command name: %s", name)
        return self.plugins.get(name)

    def get_all_plugins(self):
        """
        Retrieve all loaded plugins.

        Returns:
            dict: A dictionary of all loaded plugins.
        """
        self.logger.debug("Retrieving all loaded plugins.")
        return self.plugins
