import geo as g
import sys

def ccw(p0, p1, p2):
    dx1 = p1.x - p0.x
    dx2 = p2.x - p0.x
    dy1 = p1.y - p0.y
    dy2 = p2.y - p0.y

    if dx1 * dy2 > dy1 * dx2: return 1
    if dx1 * dy2 < dy1 * dx2: return -1
    if dx1==0 and dy1==0: return 0
    if (dx1 * dx2 < 0) or (dy1 * dy2 < 0) : return -1
    if (dx1 * dx1 + dy1 * dy2) < (dx2 * dx2 + dy2 * dy2): return 1
    return 0

def intersect(l1, l2):
    t1 = ccw(l1.p1, l1.p2, l2.p1) * ccw(l1.p1, l1.p2, l2.p2)
    t2 = ccw(l2.p1, l2.p2, l1.p1) * ccw(l2.p1, l2.p2, l1.p2)
    return t1 <= 0 and t2 <= 0

def theta(p1, p2):
    dx = p2.x - p1.x
    ax = abs(dx)
    dy = p2.y - p1.y
    ay = abs(dy)

    if ax + ay == 0: t = 0
    else: t = dy / (ax + ay)
    if dx < 0: t = 2 - t
    elif dy < 0: t = 4 + t
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
    lt = g.line()
    lp = g.line()
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
            if intersect(lp, lt) : count += 1
    return count % 2

def printInside(t, res):
    print('점 %s (%s, %s): '%(t.c,t.x, t.y), end = ' ')
    if res: 
        print('내부')
    else: print('외부')

N = 4
t = g.point(None, None, None)
p = []
p.append(g.point(None, None, None))
p.append(g.point(g.x_value[10], g.y_value[10], g.c_value[10]))
p.append(g.point(g.x_value[11], g.y_value[11], g.c_value[11]))
p.append(g.point(g.x_value[12], g.y_value[12], g.c_value[12]))
p.append(g.point(g.x_value[15], g.y_value[15], g.c_value[15]))
'''for i in range(N):
    p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))'''
p.append(g.point(None, None, None))
minIndex = 1
for i in range(2, N + 1):
    if p[i].y < p[minIndex].y:
        minIndex = i

p[minIndex], p[1] = p[1], p[minIndex]
selectionSort(p, N)

for i in range(0,16):
    if i==10 or i==11 or i==12 or i==15:
        continue
    t.x=g.x_value[i]
    t.y=g.y_value[i]
    t.c=g.c_value[i]
    printInside(t,inside(t,p,N))
'''t.x, t.y = 13, 4
printInside(t, inside(t, p, N))
t.x, t.y = 7, 9
printInside(t, inside(t, p, N))
t.x, t.y = 5, 8
printInside(t, inside(t, p, N))
t.x, t.y = 8, 13
printInside(t, inside(t, p, N))'''