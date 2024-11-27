
from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract Command Class"""

    @abstractmethod
    def execute(self):
        ...

