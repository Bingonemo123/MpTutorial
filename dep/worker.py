from dep.gui import Vis

class Worker:
    def __init__(self):
        self.x = 0
        self.gui = Vis(self)
    def run(self):
        while True:
            self.x += 1
