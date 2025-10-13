class Point:
    point_cnt = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.point_cnt += 1
        #print(self.x, self.y, self.point_cnt)

    def print_info(self):
        print(self.x, self.y, self.point_cnt)

pnt_1 = Point(1, 2)
pnt_2 = Point(4, 6)
pnt_3 = Point()

pnt_1.print_info()
pnt_2.print_info()
pnt_3.print_info()
print(Point.point_cnt)
