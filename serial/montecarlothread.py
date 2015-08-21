__author__ = 'manap'

from montecarlo import Montecarlo
import threading
import sys
from threading import Thread, Lock


def worker(num, counter):
    m = Montecarlo(counter.steps)
    m.compute()
    counter.add_hits(m.steps, m.hit, num)
    return


class MontecarloCounter:
    def __init__(self, steps=300000):
        self.total_steps = 0
        self.total_hits = 0
        self.lock = Lock()
        self.steps = steps

    def add_hits(self, new_steps, new_hits, num):
        self.lock.acquire()
        try:
            self.total_steps += new_steps
            self.total_hits += new_hits
            print  "worker %d  hits: %d  steps %d" % (num, new_hits, new_steps)

        finally:
            self.lock.release()

    def compute(self):
        self.pi = 4 * self.total_hits / (self.total_steps * 1.0)


if len(sys.argv) > 1:
    num_threads = int(sys.argv[1])
else:
    num_threads = 10
c = MontecarloCounter()

for i in range(num_threads):
    t = Thread(target=worker, args=(i, c,))
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

c.compute()
print c.pi
