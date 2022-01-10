with open("08.txt") as f:
    data = f.read().split("\n")[:-1]

a = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
b = "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"
c = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

signals_to_digits = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

class Display:
    def __init__(self, s):
        self.patterns = list(map(set, s.split(" | ")[0].split(" ")))
        self.output = list(map(set, s.split(" | ")[1].split(" ")))
        self.occurences = self.get_occurences()
        self.mapping = {}
        self.deduce_mapping()
        self.map_patterns_to_digits()

    def get_output(self):
        result = ""
        for out in self.output:
            result += str(self.digits["".join(sorted(out))])
        return int(result)

    def deduce_mapping(self):
        self.deduce_cf()
        self.deduce_a()
        self.deduce_be()
        self.deduce_d()
        self.deduce_g()

    def map_patterns_to_digits(self):
        self.digits = {}
        for pattern in self.patterns:
            real = ""
            for c in pattern:
                real += self.mapping[c]
            real = "".join(sorted(real))
            self.digits["".join(sorted(pattern))] = signals_to_digits[real.lower()]

    def deduce_cf(self):
        one_pattern = list(list(filter(lambda x: len(x) == 2, self.patterns))[0])
        contains_a = len(list(filter(lambda x: one_pattern[0] in x, self.patterns)))
        if contains_a == 8:
            self.mapping[one_pattern[0]] = "C"
            self.mapping[one_pattern[1]] = "F"
        else:
            self.mapping[one_pattern[0]] = "F"
            self.mapping[one_pattern[1]] = "C"

    def deduce_a(self):
        seven_pattern = self.find_pattern_with_n_segments(3)
        for signal in seven_pattern:
            if signal not in self.mapping:
                self.mapping[signal] = "A"

    def deduce_be(self):
        for c in "abcdefg":
            if self.occurences[c] == 6:
                self.mapping[c] = "B"
            elif self.occurences[c] == 4:
                self.mapping[c] = "E"

    def deduce_d(self):
        four_pattern = self.find_pattern_with_n_segments(4)
        for signal in four_pattern:
            if signal not in self.mapping:
                self.mapping[signal] = "D"

    def deduce_g(self):
        for c in "abcdefg":
            if c not in self.mapping:
                self.mapping[c] = "G"

    def get_occurences(self):
        result = {}
        for c in "abcdefg":
            result[c] = len(list(filter(lambda x: c in x, self.patterns)))
        return result

    def find_pattern_with_n_segments(self, n):
        return list(list(filter(lambda x: len(x) == n, self.patterns))[0])

    def number_of_1478_in_output(self):
        return len(list(filter(lambda x: len(x) in [2, 3, 4, 7], self.output)))

    def print_mappings(self):
        for key in self.mapping:
            print(f"{key} -> {self.mapping[key]}")
        print("DIGITS:", self.digits)

total = 0
for line in data:
    d = Display(line)
    total += d.get_output()
print(total)

# 1 -> 2

# 7 -> 3

# 4 -> 4

# 2 -> 5
# 3 -> 5
# 5 -> 5

# 0 -> 6
# 6 -> 6
# 9 -> 6

# 8 -> 7
