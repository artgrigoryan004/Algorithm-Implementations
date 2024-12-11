
def graham_scan(points):
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    start = min(points, key=lambda p: (p[1], p[0]))
    points.pop(points.index(start))
    points.sort(key=lambda p: (-(p[1] - start[1]) / ((p[0] - start[0]) or 1), p[0]))
    hull = [start]
    for p in points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

# Example
points = [(0, 0), (1, 1), (2, 2), (2, 0), (2, 4), (3, 3), (0, 4)]
print(graham_scan(points))

