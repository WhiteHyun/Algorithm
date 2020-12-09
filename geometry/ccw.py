from Point import Point
import random


def ccw(p0, p1, p2, return_case=False):
    dx1 = p1.x - p0.x
    dy1 = p1.y - p0.y
    dx2 = p2.x - p0.x
    dy2 = p2.y - p0.y

    case = 0
    ret = 0

    if dx1*dy2 > dy1*dx2:
        case = 0
        ret = 1
    elif dx1*dy2 < dy1*dx2:
        case = 1
        ret = -1
    elif dx1 == 0 and dy1 == 0:
        case = 2
        ret = 0
    elif dx1*dx2 < 0 or dy1*dy2 < 0:
        case = 3
        ret = -1
    elif dx1**2+dy1**2 < dx2**2+dy2**2:
        case = 4
        ret = 1
    else:
        case = 5
        ret = 0

    if return_case:
        return case
    else:
        return ret


if __name__ == "__main__":
    cases = [[], [], [], [], [], []]

    points = Point.create_random_points(size=20, n_points=20)
    points += Point.create_random_points(size=20, n_points=20)
    points += Point.create_random_points(size=20, n_points=20)

    for i in range(0, 60):
        p0 = random.choice(points)
        p1 = random.choice(points)
        p2 = random.choice(points)

        cases[ccw(p0, p1, p2, return_case=True)].append((p0, p1, p2))

    for i in range(0, 6):
        print(
            "===================== Case {num} =====================".format(num=i+1))
        triples = cases[i]
        for triple in triples:
            print("p0 = {p0}, p1 = {p1}, p2 = {p2}".format(
                p0=triple[0], p1=triple[1], p2=triple[2]))
        print("\n"*2)
