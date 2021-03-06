with open("02.txt") as f:
    data = f.read().split("\n")[:-1]

x = 0
y = 0
aim = 0

for command in data:
    (operation, amount) = command.split(" ")
    amount = int(amount)
    if operation == "forward":
        x += amount
        y += aim * amount
    elif operation == "down":
        aim += amount
    elif operation == "up":
        aim -= amount

print(x*y)
