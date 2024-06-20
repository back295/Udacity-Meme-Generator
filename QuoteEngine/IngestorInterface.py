from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """ Abstract base class for the ingestor superclass"""

    valid_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file type is valid"""
        extension = path.split('.')[-1]
        return True if extension in cls.valid_extensions else False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Empty abstract function. We will define this function later
            in the superclass
        """
        pass
