with open("03.txt") as f:
    data = f.read().split("\n")[:-1]

width = len(data[0])

ones = width * [0]

for line in data:
    for bit in range(width):
        if line[bit] == "1":
            ones[bit] += 1

for bit in range(width):
    if ones[bit] > len(data)/2:
        ones[bit] = 1
    else:
        ones[bit] = 0

gamma = 0
for bit in range(width):
    gamma += ones[bit] << (width - 1 - bit)
epsilon = ~gamma & 0xfff

print(gamma*epsilon)
