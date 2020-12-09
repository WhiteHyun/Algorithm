import geo as g


def theta(p1, p2):
    """
    p1을 기점으로 p2의 위치가 몇 도가량에 위치되어있는지 확인해주는 함수
    """
    dx = p2.x - p1.x
    ax = abs(dx)
    dy = p2.y - p1.y
    ay = abs(dy)
    if ax+ay == 0:
        t = 0
    else:
        t = dy / (ax + ay)

    if dx < 0:
        t = 2-t
    elif dy < 0:
        t += 4
    return t*90


def package_wrapping(p, n):
    min_index = 0
    for i in range(n):
        if p[i].y < p[min_index].y:
            min_index = i
    p[n] = p[min_index]
    th = 0.0
    for m in range(n):
        p[m], p[min_index] = p[min_index], p[m]
        min_index = n
        v = th
        th = 360.0
        for i in range(m+1, n+1):
            if theta(p[m], p[i]) > v:
                if theta(p[m], p[i]) < th:
                    min_index = i
                    th = theta(p[m], p[min_index])
        if min_index == n:
            return m


if __name__ == "__main__":
    N = 8
    p = []
    for i in range(N):
        p.append(g.point(g.x_value[i], g.y_value[i], g.c_value[i]))
    p.append(g.point(None, None, None))
    M = package_wrapping(p, N)
    for i in range(M+1):
        print(p[i].c, end=' ')
