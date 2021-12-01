with open("01.txt") as f:
    data = f.read().split("\n")[:-1]

data = list(map(int, data))

increases = 0

for i in range(len(data) - 3):
    if(data[i]+data[i+1]+data[i+2] < data[i+1]+data[i+2]+data[i+3]):
        increases += 1

print(increases)
