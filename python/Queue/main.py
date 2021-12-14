from queue_utils import QueueUtils
from qustom_queue import Queue
from figures import Point, Circle

points = Queue[Point]()

point1, point2, point3 = Point("abc"), Point("def"), Point("ghi")

points.add(point1)
points.add(point2)
points.add(point3)

circles = Queue[Circle]()
circles2 = Queue[Circle]()

circle1, circle2, circle3 = Circle("123"), Circle("456"), Circle("789")

circles.add(circle1)
circles.add(circle2)
circles.add(circle3)

queue_all = Queue()

for item in ["asdgfd", 12432, "dsa", "cxz", 321.22]:
    queue_all.add(item)

utils = QueueUtils()
utils.printAndClear(queue_all)

utils.printFiguresAndClear(points)

utils.move(circles, circles2)
utils.printFiguresAndClear(circles2)
