import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Superclass for Docx files"""

    valid_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Load qoutes from Docx files

        Arguments:
            path {str} : path to the .docx file.
        """
        if not cls.can_ingest(path):
            raise Exception("DocxIngestor: Can ingest the docx file only!")

        quotes = []
        doc_file = docx.Document(path)

        for text in doc_file.paragraphs:
            if text.text:
                parse = text.text.split(' - ')
                quote = QuoteModel(parse[0].strip('"'), parse[1])
                quotes.append(quote)

        return quotes
