import geo as g
import sys


def ccw(p0, p1, p2):
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


def selection_sort(p, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i+1, n+1):
            if theta(p[1], p[j]) < theta(p[1], p[minIndex]):
                minIndex = j
        p[minIndex], p[i] = p[i], p[minIndex]


def graham_scan(p, n):
    min_index = 1
    for i in range(2, n+1):
        if p[i].y < p[min_index].y:
            min_index = i
    for i in range(1, n+1):
        if p[i].y == p[min_index].y:
            if p[i].x > p[min_index].x:
                min_index = i
    p[1], p[min_index] = p[min_index], p[1]
    selection_sort(p, n)
    p[0] = p[n]
    m = 3
    for i in range(4, n+1):
        while ccw(p[m], p[m-1], p[i]) >= 0:  # 우회전일 경우
            # print(g.c_value[m], g.c_value[m-1], g.c_value[i])
            print(p[m].c, p[m-1].c, p[i].c)
            m -= 1
        m += 1
        p[i], p[m] = p[m], p[i]
    return m


if __name__ == "__main__":
    N = 16
    p = []
    p.append(g.point(0, 0, None))
    for i in range(N):
        p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))
    M = graham_scan(p, N)
    # for i in range(1, M+1):
    #     print(p[i].c, end=' ')
