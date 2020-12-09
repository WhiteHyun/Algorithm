# Run for script only.
from Point import Point


def theta(p0, p1):
    """
    >>> theta(Point(2, 2), Point(5, 5))
    45.0
    >>> theta(Point(5, 5), Point(2, 2))
    225.0
    >>> theta(Point(3, 2), Point(1, 5))
    125.99999999999999
    >>> theta(Point(9, 1), Point(7, 4))
    125.99999999999999
    >>> theta(Point(5, 2), Point(8, 5))
    45.0
    """
    dx = p1.x - p0.x
    dy = p1.y - p0.y
    if dx == 0 and dy == 0:
        return None

    ax = abs(dx)
    ay = abs(dy)

    atotal = ax + ay
    t = (dy / atotal) if atotal != 0 else 0

    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t = 4 + t

    return t * 90


def package_wrapping(points):
    min_index = points.index(min(points, key=lambda p: p.y))
    angle_min = 0.0

    points.append(points[min_index])
    n = len(points)

    for sorted_index in range(0, n):
        points[sorted_index], points[min_index] = points[min_index], points[sorted_index]
        angle_last = angle_min
        angle_min = 360.0

        for i in range(sorted_index + 1, n):
            angle = theta(points[sorted_index], points[i])

            # When to points are identical.
            if angle is None:
                continue

            # When the end line is horizontal.
            # The angle must be incremental.
            # If the last line is horizontal, the line before it must be
            # close to 360, so the last angle must be 360.
            if angle == 0.0 and i == n - 1:
                angle = 360.0

            # When found new min angle.
            if angle >= angle_last and angle <= angle_min:
                min_index = i
                angle_min = angle

        if min_index == n - 1:
            points.pop()
            return sorted_index + 1

    # Must NOT reach here.
    print("ERROR")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    points = Point.create_random_points(size=16, n_points=16)
    n_dots = package_wrapping(points)
    for i in range(0, n_dots):
        points[i].shape = '@'

    Point.dump_points(points)
