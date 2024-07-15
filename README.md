# Meme Generator #

## Overview ##

Meme generator is used to generate memes. The meme is including an image with a quote.

This project has common features in Python to practice what I have learned in the Advance Python course of Udacity, including:

- OOP in Python, such as class, object, abstract classes, class methods and static methods.

- Syntax of Python, like if/else, try/except, function ...

- Modules and packages in Python.

- File handling in Python, including .txt, .csv, .pdf, .png ...

## Module Desciptions ##

### QuoteEngine ###

The `QuoteEngine` module is responsible for ingesting various types of file (including .txt, .csv, .docs, .pdf), which contains quotes. This module has several classes (`QuoteModel`, `CSVIngestor`, `DocxIngestor`, `PDFIngestor`, `TextIngestor`, `Ingestor` and `IngestorInterface`). Those classes demonstrates that what I have learned in Python.

The brief of each class is described as below:

- `IngestorInterface`: is a abstract base class. It contains some helper functions, which is defined in the superclass.

- `Ingestor`: is used for handling variety types of the file. It can select the appropiate helper function for each type of file.

- `QuoteModel`: represent for a quote, including two part. One is body, and the other is author of the quote.

- `SVIngestor`, `DocxIngestor`, `PDFIngestor`, `TextIngestor`: Each class is responsible for handling respective type of the file.

### MemeEngine ###

The `MemeEngine` is accountable for generating memes. For detailed, this module can open available images, resize and draw a quote on each of them. Finally, the meme images is stored into the `./static` folder with the random name. 

The images is handled by the `Pillow` module.

### Command Line Interface ###

        usage: meme.py [-h] [--body BODY] [--author AUTHOR] [--path PATH]

The meme.py script has three optional CLI arguments:

- --body a string quote 

- --author a string quote author

- --path an image path

The script returns a path to a generated image. If any argument is not defined, a random selection is used.

## Instructions ##

### Setup ###

To run the project, you should follow bellow steps:

- Clone this prository using the command : `git clone https://github.com/back295/Udacity-Meme-Generator.git`

- Create a virtual environment and install specific requirements:

        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt

### Flask Web Service ###

To start the app on your local machine:

        export FLASK_APP=app.py
        flask run --host 0.0.0.0 --port 3000 --reload

Then open the web browser and enter the link address: `http://localhost:3000` to go the web page.
