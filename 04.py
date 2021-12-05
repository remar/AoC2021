with open("04.txt") as f:
    data = f.read().split("\n")[:-1]

    
print(data)

numbers = [int(x) for x in data[0].split(",")]

print(numbers)

class Board:
    def __init__(self, lines):
        self.lines = []
        self.marks = [5*[False] for x in range(5)]
        for line in lines:
            self.insert_line(line)

    def insert_line(self, line):
        self.lines.append(list(map(int, filter(lambda x: x, line.split(" ")))))

    def mark(self, number):
        for y in range(5):
            for x in range(5):
                if self.lines[y][x] == number:
                    self.marks[y][x] = True

    def wins(self):
        for mark_line in self.marks:
            if all(mark_line):
                return True
        for mark_column in list(zip(*self.marks)):
            if all(mark_column):
                return True

    def unmarked_sum(self):
        total = 0
        for y in range(5):
            for x in range(5):
                if not self.marks[y][x]:
                    total += self.lines[y][x]
        return total

    def __str__(self):
        return ("\n".join(list(map(lambda x: str(x), self.lines)))
                + "\n"
                + "\n".join(list(map(lambda x: str(x), self.marks))))

boards = []

data_index = 2

while data_index < len(data):
    boards.append(Board(data[data_index:data_index+5]))
    data_index += 6

for number in numbers:
    for board in boards:
        board.mark(number)
        if board.wins():
            print("WOOOOO!", number*board.unmarked_sum())
            exit()
