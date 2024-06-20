from typing import List

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CannotIngest(Exception):
    """Raised when the type of ingested file is not valid."""

    def __init__(self, message):
        self.message = message


class Ingestor(IngestorInterface):
    """This class encapsulates all the Ingestor classes.

       It should realize the IngestorInterface strategy.
    """

    # List of ingestors
    ingestors = [CSVIngestor, TextIngestor, PDFIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create list of quotes from various file types"""
        should_ingest = False

        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                should_ingest = True
                return ingestor.parse(path)

        if not should_ingest:
            raise CannotIngest(f"Cannot ingest {path} file")
