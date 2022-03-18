import multiprocessing as mp
from dep.worker import Worker
from dep.gui import Vis

w = Worker()
v = Vis()

if __name__ == '__main__':
    p1 = mp.Process(target=w.run)
    p2 = mp.Process(target=v.loop_flow)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


