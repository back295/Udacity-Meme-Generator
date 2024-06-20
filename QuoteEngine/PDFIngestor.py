from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Superclass for CSV files"""

    valid_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Load qoutes from PDF files

        Arguments:
            path {str} : path to the .pdf file.
        """

        if not cls.can_ingest(path):
            raise Exception("PDFIngestor: Can ingest the .pdf files only!")

        quotes = []

        temp = str(random.randint(0, 1000)) + ".txt"
        call = subprocess.run(['pdftotext', path, temp])

        with open(temp, "r") as text_file:
            for line in text_file:
                if line:
                    try:
                        body, author = line.strip().split(" - ")
                    except ValueError:
                        pass
                    else:
                        quote = QuoteModel(body.strip('"'), author)
                        quotes.append(quote)

        # Remove temporary text file
        os.remove(temp)

        return quotes
