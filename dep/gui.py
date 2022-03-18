import time

class Vis():
    def __init__(self, lu):
        self.lu = lu

    def loop_flow(self):
        while True:
            print(self.lu.x)
            time.sleep(1)
            
