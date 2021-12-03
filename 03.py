with open("03.txt") as f:
    data = f.read().split("\n")[:-1]

width = len(data[0])

def ones_in_column(column, data):
    ones = 0
    for line in data:
        if line[column] == "1":
            ones += 1
    return ones

oxygen_data = list(data)

for column in range(width):
    ones = ones_in_column(column, oxygen_data)
    zeros = len(oxygen_data) - ones
    if ones >= zeros:
        oxygen_data = list(filter(lambda x: x[column] == "1", oxygen_data))
    else:
        oxygen_data = list(filter(lambda x: x[column] == "0", oxygen_data))
#    print(column, oxygen_data)
    if len(oxygen_data) == 1:
        oxygen = int(oxygen_data[0], 2)
        break


co2_data = list(data)

for column in range(width):
    ones = ones_in_column(column, co2_data)
    zeros = len(co2_data) - ones
    if ones >= zeros:
        co2_data = list(filter(lambda x: x[column] == "0", co2_data))
    else:
        co2_data = list(filter(lambda x: x[column] == "1", co2_data))
    print(len(co2_data))
    if len(co2_data) == 1:
        co2 = int(co2_data[0], 2)
        break


print(oxygen*co2)
