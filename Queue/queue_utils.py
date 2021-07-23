from figures import Figure
from qustom_queue import Queue


class QueueUtils(Queue):

    def printAndClear(self, queue: Queue) -> None:
        while not queue.isEmpty():
            item = queue.get()
            print(item)

    def printFiguresAndClear(self, queue: Queue[Figure]) -> None:
        while not queue.isEmpty():
            item = queue.get()
            print(item)

    def move(self, source: Queue, dest: Queue) -> None:
        if source.__class__ == dest.__class__:
            while not source.isEmpty():
                item = source.get()
                dest.add(item)
        else:
            raise Exception("error different types of queues")
