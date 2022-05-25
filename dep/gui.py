import time

class Vis():
    def __init__(self, lu):
        self.lu = lu

    def loop_flow(self, lu):
        while True:
            self.lu = lu
            print(self.lu.x)
            time.sleep(1)
            
