import pandas
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Superclass for CSV files"""

    valid_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Load qoutes from files

        Arguments:
            path {str} : path to the .csv file.
        """

        if not cls.can_ingest(path):
            raise Exception("CSVIngestor: Can ingest .csv file only!")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row["body"], row["author"])
            quotes.append(quote)

        return quotes
