import os
import random

from QuoteEngine import QuoteModel, Ingestor, CannotIngest
from MemeEngine import MemeGenerator
import argparse


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./static')
    path = meme.generate_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    """Self CLI interface definition"""

    parser = argparse.ArgumentParser(description="MEME GENERATOR")
    parser.add_argument("--path", type=str, help="The path to image folder")
    parser.add_argument("--body", type=str, help="The body of the quote")
    parser.add_argument("--author", type=str, help="The author of the quote")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
