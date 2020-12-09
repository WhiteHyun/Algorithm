import geo as g

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

def printLine(l1,l2,result):
    print('선분 %s%s와 선분 %s%s은 '%(l1.p1.c,l1.p2.c,l2.p1.c,l2.p2.c),end='')
    if result:
        print('교차함')
    else:
        print('교차하지 않음')

N=16
p=[]
p.append(g.point(None,None,None))
for i in range(N):
    p.append(g.point(g.x_value[i],g.y_value[i],g.c_value[i]))
l1=g.line()
l2=g.line()
l1.p1=p[1]
l1.p2=p[15]
l2.p1=p[3]
l2.p2=p[14]
result=intersect(l1,l2)
printLine(l1,l2,result)