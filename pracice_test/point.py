import sys


class point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c


class line:
    def __init__(self):
        self.p1 = point(None, None, None)
        self.p2 = point(None, None, None)


def ccw(p0, p1, p2):
    """시계 반대 방향 검사 알고리즘"""
    dx1 = p1.x - p0.x
    dx2 = p2.x - p0.x
    dy1 = p1.y - p0.y
    dy2 = p2.y - p0.y

    if dx1 * dy2 > dy1 * dx2:
        return 1
    if dx1 * dy2 < dy1 * dx2:
        return -1
    if dx1 == 0 and dy1 == 0:
        return 0
    if (dx1 * dx2 < 0) or (dy1 * dy2 < 0):
        return -1
    if (dx1 * dx1 + dy1 * dy2) < (dx2 * dx2 + dy2 * dy2):
        return 1
    return 0


def intersect(l1, l2):
    """선분 교차 여부 검사 알고리즘"""
    t1 = ccw(l1.p1, l1.p2, l2.p1) * ccw(l1.p1, l1.p2, l2.p2)
    t2 = ccw(l2.p1, l2.p2, l1.p1) * ccw(l2.p1, l2.p2, l1.p2)
    return t1 <= 0 and t2 <= 0


def theta(p1, p2):
    dx = p2.x - p1.x
    ax = abs(dx)
    dy = p2.y - p1.y
    ay = abs(dy)

    if ax + ay == 0:
        t = 0
    else:
        t = dy / (ax + ay)
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t
    return 90 * t


def selectionSort(p, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i + 1, n + 1):
            if theta(p[1], p[j]) < theta(p[1], p[minIndex]):
                minIndex = j
        p[minIndex], p[i] = p[i], p[minIndex]


def inside(t, p, n):
    count = 0
    j = 0
    lt = line()
    lp = line()
    p[0] = p[n]
    p[n+1] = p[1]
    lt.p1 = t
    lt.p2.x = sys.maxsize
    lt.p2.y = t.y
    for i in range(1, n + 1):
        lp.p1 = p[i]
        lp.p2 = p[i]
        if not intersect(lp, lt):
            lp.p2 = p[j]
            j = i
            if intersect(lp, lt):
                count += 1
    return count % 2


def printInside(t, res):
    if res:
        print('내부')
    else:
        print('외부')


x_value = [2, 12, 3, 10, 14, 1, 13, 6, 8, 7, 15, 16, 4, 11, 9, 5]
y_value = [6, 16, 12, 11, 4, 10, 8, 7, 9, 5, 3, 14, 15, 1, 13, 2]
c_value = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


if __name__ == "__main__":
    N = 4
    t = point(None, None, None)
    p = []
    p.append(point(None, None, None))
    for i in [10, 11, 12, 15]:
        p.append(point(x_value[i], y_value[i], c_value[i]))
    p.append(point(None, None, None))
    minIndex = 1
    for i in range(2, 4 + 1):
        if p[i].y < p[minIndex].y:
            minIndex = i

    p[minIndex], p[1] = p[1], p[minIndex]
    selectionSort(p, N)

    for i in range(16):
        if i in [10, 11, 12, 15]:
            continue
        t.x, t.y = x_value[i], y_value[i]
        print(f'점 {c_value[i]} ({x_value[i]}, {y_value[i]}) : ', end='')
        printInside(t, inside(t, p, 4))
