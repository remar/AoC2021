import functools

with open("09.txt") as f:
    data = f.read().split("\n")[:-1]

width = len(data[0])
height = len(data)

def get(x, y):
    if x >= 0 and x < width and y >= 0 and y < height:
        return int(data[y][x])
    return 10

def is_low_point(x, y):
    val = get(x, y)
    return val < get(x-1,y) and val < get(x+1,y) and val < get(x,y-1) and val < get(x,y+1)

print(is_low_point(1, 0))

def find_low_points():
    result = []
    for y in range(height):
        for x in range(width):
            if is_low_point(x, y):
                result.append((x, y))
    return result

print(find_low_points())

def flood_fill_from(x, y):
    visited = set()
    edges = []
    def flood_fill_internal(x, y):
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if (x, y) in visited:
            return
        visited.add((x, y))
        if get(x, y) == 9:
            edges.append((x, y))
            return
        flood_fill_internal(x-1,y)
        flood_fill_internal(x+1,y)
        flood_fill_internal(x,y-1)
        flood_fill_internal(x,y+1)

    flood_fill_internal(x, y)
    return len(visited) - len(edges)

sizes = []
for point in find_low_points():
    sizes.append(flood_fill_from(point[0], point[1]))

print(functools.reduce(lambda a, b: a*b, sorted(sizes)[-3:]))
