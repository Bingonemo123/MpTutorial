import multiprocessing as mp
from dep.worker import Worker
from dep.gui import Vis

w = Worker()

if __name__ == '__main__':
    p1 = mp.Process(target=w.run)
    p2 = mp.Process(target=w.gui.loop_flow, args=(w,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


