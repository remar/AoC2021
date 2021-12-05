with open("05.txt") as f:
    data = f.read().split("\n")[:-1]

def parse_line(line):
    return ([list(map(int, x.split(","))) for x in line.split(" -> ")])

points = {}

def get_direction(dir):
    if dir < 0:
        return -1
    elif dir > 0:
        return 1
    else:
        return 0

def add_point(x, y):
    pos_tuple = (x, y)
    if pos_tuple in points:
        points[pos_tuple] += 1
    else:
        points[pos_tuple] = 1
    
for line in data:
    l = parse_line(line)
    pos = list(l[0])
    delta = [get_direction(l[1][0] - l[0][0]), get_direction(l[1][1] - l[0][1])]
    while pos != l[1]:
        add_point(pos[0], pos[1])
        pos[0] += delta[0]
        pos[1] += delta[1]
    add_point(l[1][0], l[1][1])

print("result:", len(list(filter(lambda x: x > 1, points.values()))))
