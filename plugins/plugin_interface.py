from abc import ABC, abstractmethod

class CommandPlugin(ABC):
    """Abstract base class for command plugins."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute the command."""
        pass

    @abstractmethod
    def get_command_name(self) -> str:
        """Return the name of the command."""
        pass
