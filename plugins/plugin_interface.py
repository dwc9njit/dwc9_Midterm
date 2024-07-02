# plugin_interface.py
"""
This module provides help functionalities for the application.
"""

# plugin_interface.py
from abc import ABC, abstractmethod

class CommandPlugin(ABC):
    """Abstract base class for command plugins."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute the command."""
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def get_command_name(self) -> str:
        """Return the name of the command."""
        raise NotImplementedError("This method should be overridden by subclasses")
