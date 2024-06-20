from random import randint
from PIL import Image, ImageDraw, ImageFont
import exception


class MemeGenerator:
    """The meme generator class is used to generate meme images

    Arguments:
        output_dir {str} -- the folder path to save the output images.
    """

    def __init__(self, output) -> None:
        self.output = output

    def generate_meme(self, img_path: str, quote: str,
                      author: str, width: int = 500) -> str:
        """Create a Meme image with Quotes

        Arguments:
            img_path {str} -- path to input images.
            quote {str} -- the body of quotes.
            author {str} -- the author of quotes.
            width {int} -- The pixel width value.
        Returns:
            str -- the file path to the output images.
        """

        try:
            with Image.open(img_path) as image:
                if width:
                    ratio = width / float(image.size[0])
                    height = int(ratio * float(image.size[1]))
                    image = image.resize((width, height), Image.NEAREST)
                    font_size = int(image.height / 20)

                # Add quote to the meme image
                if(quote, author):
                    text = f"{quote} \n - {author}"
                    draw = ImageDraw.Draw(image)
                    font = ImageFont.truetype("../arial.ttf", font_size)
                    x = randint(0, int(image.width/10))
                    y = randint(0, int(image.height-font_size*2))
                    draw.text((x, y), text, font=font, fill='green')

                # Save image
                image_out_name = f"{randint(0,1000)}.jpg"
                image_out_path = f"{self.output}/{image_out_name}"
                image.save(image_out_path)
        except exception:
            raise ValueError("Invalid image file path!")

        return image_out_path
