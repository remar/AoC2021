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
                result.append(get(x, y))
    return result

print(sum(map(lambda x: x + 1, find_low_points())))
