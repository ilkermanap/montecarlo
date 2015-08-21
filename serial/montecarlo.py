from random import random
import sys


class Montecarlo:
    def __init__(self, steps=1000):
        self.steps = steps
        self.hit = 0
        self.miss = 0
        self.pi = None
        self.points = []
        self.compute()

    def compute(self):
        for i in range(self.steps):
            x = 2 * random() - 1
            y = 2 * random() - 1
            self.points.append((x, y))
            if ((x ** 2) + (y ** 2)) <= 1:
                self.hit += 1
            else:
                self.miss += 1

        self.pi = 4 * (self.hit / (self.steps * 1.0))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])
        m = Montecarlo(steps)
        print m.pi

    else:
        m = Montecarlo()
        print m.pi
