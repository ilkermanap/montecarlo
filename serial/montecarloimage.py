__author__ = 'manap'

from PIL import Image, ImageDraw
from montecarlo import Montecarlo


class MontecarloImage(Montecarlo):
    def __init__(self, steps):
        Montecarlo.__init__(self, steps)
        self.image = Image.open("arc.png")
        self.draw = ImageDraw.Draw(self.image)

    def draw_points(self):
        for point in self.points:
            x, y = point
            x = abs(int(x * 800))
            y = abs(int(y * 800))
            self.image.putpixel((x, y), (255, 0, 0))
        self.image.save("test.png")


x = MontecarloImage(50000)
x.compute()
x.draw_points()
