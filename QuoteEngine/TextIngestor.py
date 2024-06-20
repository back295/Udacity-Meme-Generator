from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Superclass for text files"""
    valid_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Get quote from text files

        Arguments:
            path {str} -- path to the text file.
        """
        if not cls.can_ingest(path):
            raise Exception("TextIngestor: Can ingest the text file only!")

        quotes = []

        with open(path, "r") as text_file:
            for line in text_file:
                try:
                    body, author = line.split(" - ")
                except ValueError:
                    pass
                else:
                    quote = QuoteModel(body=body.strip('"'),
                                       author=author.strip())
                    quotes.append(quote)

        return quotes
