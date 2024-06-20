class QuoteModel:
    """Quotes to add to memes later."""

    def __init__(self, body: str, author: str) -> None:
        """Build quote objects

        Arguments:
            body {str} -- the actual quote message.
            author {str} -- Author of the quote.
        """

        self.author = author
        self.body = body

    def __str__(self):
        """Printf quote"""
        return f'"{self.body}" <- {self.author}'
