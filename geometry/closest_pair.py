import geo as g
import math

temp_min = 0


class node:
    def __init__(self):
        self.p = g.point(max, max, '')
        self.next = None


def comp(t):
    if (t_pass == 1):
        return t.p.x
    else:
        return t.p.y


def merge(a, b):
    c = z
    while(True):
        if(comp(a) < comp(b)):
            c.next = a
            c = a
            a = a.next
        else:
            c.next = b
            c = b
            b = b.next

        if (c == z):
            break

    c = z.next
    z.next = z
    return c


def check(p1, p2):
    global min, cp1, cp2, temp_min
    if(p1.y != z.p.y) and (p2.y != z.p.y):
        dist = (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y)
        if (math.sqrt(dist) < min):
            temp_min = dist
            min = math.sqrt(dist)
            cp1 = p1
            cp2 = p2


def sort(c, N):
    if(c.next == z):
        return c
    a = c
    for i in range(2, int(N/2)+1):
        c = c.next
    b = c.next
    c.next = z
    temp_middle = c
    c = merge(sort(a, int(N/2)), sort(b, N - int(N/2)))

    if (t_pass == 2):
        middle = temp_middle.p.x
        p1 = z.p
        p2 = z.p
        p3 = z.p
        p4 = z.p
        a = c
        while(a != z):
            if (math.fabs(a.p.x - middle) < min):
                check(a.p, p1)
                check(a.p, p2)
                check(a.p, p3)
                check(a.p, p4)
                p1 = p2
                p2 = p3
                p3 = p4
                p4 = a.p
                print(
                    f'r({temp_min:^5}){cp1.c:^5}{cp2.c:^5}{p1.c:^5}{p2.c:^5}{p3.c:^5}{p4.c:^5}')
            a = a.next

    return c


def readlist():
    p = node()
    h = p
    for i in range(N):
        t = node()
        t.p.x = g.x_value[i]
        t.p.y = g.y_value[i]
        t.p.c = g.c_value[i]
        p.next = t
        p = p.next
    p.next = z
    return h


N = 8
max = 1000
cp1 = g.point(max, max, '')
cp2 = g.point(max, max, '')
min = max

z = node()
z.p.x = max
z.p.y = max
z.next = z
h = node()
h.next = readlist()

print(f"{'minvalue':^5}{'cp1':^5}{'cp2':^5}{'p1':^5}{'p2':^5}{'p3':^5}{'p4':^5}")
t_pass = 1
h.next = sort(h.next, N)
t_pass = 2
h.next = sort(h.next, N)
print('min = %.3f, cp1 = %s, cp2 = %s' % (min, cp1.c, cp2.c))
