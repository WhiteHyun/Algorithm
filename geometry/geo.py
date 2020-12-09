class point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c


class line:
    def __init__(self):
        self.p1 = point(None, None, None)
        self.p2 = point(None, None, None)


# x_value = [5, 7, 6, 8, 1, 4, 3, 2, 11, 12, 10, 9]
# y_value = [3, 11, 12, 2, 4, 10, 6, 5, 8, 9, 1, 7]
# c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
x_value = [5, 8, 3, 4, 2, 1, 7, 6]
y_value = [7, 6, 5, 1, 2, 8, 3, 4]
c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
