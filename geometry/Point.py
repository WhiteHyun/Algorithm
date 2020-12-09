import random
import itertools


class Point:
    """
    2D point.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = '+'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == self.y)

    def __hash__(self):
        return hash(('x', self.x, 'y', self.y))

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def dist_horizontal(self, other):
        return (self.x - other.x)**2

    def dist_vertical(self, other):
        return (self.y - other.y)**2

    def dist(self, other):
        return self.dist_horizontal(other) + self.dist_vertical(other)

    @staticmethod
    def create_random_points(size, n_points):
        """
        Every point is unique.
        """
        points = list()

        while len(points) < n_points:
            x = int(random.randint(0, size - 1))
            y = int(random.randint(0, size - 1))
            p = Point(x, y)
            if p not in points:
                points.append(p)

        # No duplicates.
        return points

    @staticmethod
    def dump_points(m, width=2):
        y_sorted = sorted(m, key=lambda p: p.y)
        y_indices = list(set(map(lambda p: p.y, y_sorted)))  # y dups killed.
        splited = [list(filter(lambda p: p.y == y, y_sorted))
                   for y in y_indices]
        # x dups killed.
        processed = [sorted(list(set(l)), key=lambda p: p.x) for l in splited]

        y_offset = 0
        x_offset = 0

        for row in processed:
            y = row[0].y
            to_go = y - y_offset
            print('\n'*to_go, end='')
            y_offset = y
            x_offset = 0

            for p in row:
                x = p.x
                to_go = x - x_offset - 1
                print(' '*(width*to_go), end='')
                x_offset = x
                print(str(p.shape) + ' '*(width-1), end='')

        print("")
