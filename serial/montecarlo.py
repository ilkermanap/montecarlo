from random import random
import sys


class Montecarlo:
    def __init__(self, steps=1000):
        self.steps = steps
        self.hit = 0
        self.pi = None
        self.points = []

    def add_points(self, points):
        self.points.extend(points)
        self.steps += len(points)

    def compute_from_list(self):
        self.steps = len(self.points)
        for p in self.points:
            x, y = p
            if ((x ** 2) + (y ** 2)) <= 1:
                self.hit += 1
        self.pi = 4 * (self.hit / (steps * 1.0))

    def compute(self):
        for i in range(self.steps):
            x = 2 * random() - 1
            y = 2 * random() - 1
            self.points.append((x, y))
            if ((x ** 2) + (y ** 2)) <= 1:
                self.hit += 1
        self.pi = 4 * (self.hit / (self.steps * 1.0))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        steps = int(sys.argv[1])
        m = Montecarlo(steps)
        m.compute()
        print m.pi
    else:
        m = Montecarlo(1000000)
        m.compute()
        print m.pi
