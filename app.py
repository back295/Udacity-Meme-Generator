import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import QuoteModel, Ingestor, CannotIngest
from MemeEngine import MemeGenerator

app = Flask(__name__)

m_path = "./static"

if not os.path.isdir(m_path):
    os.mkdir(m_path)

meme = MemeGenerator(m_path)


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except CannotIngest as error:
            print(f"{error.message}")

    print(quotes)
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.generate_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form.get("image_url")
    answer = requests.get(image_url, allow_redirects=True)
    temp = f"{m_path}/{random.randint(0,5000)}.png"

    with open(temp, "wb") as file:
        file.write(answer.content)
    quote = QuoteModel(request.form.get("body"), request.form.get("author"))

    path = meme.generate_meme(temp, quote.body, quote.author)
    # Remove temporary file
    os.remove(temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
