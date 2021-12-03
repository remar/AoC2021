with open("02.txt") as f:
    data = f.read().split("\n")[:-1]

x = 0
y = 0

for command in data:
    (operation, amount) = command.split(" ")
    amount = int(amount)
    if operation == "forward":
        x += amount
    elif operation == "down":
        y += amount
    elif operation == "up":
        y -= amount

print(x*y)
