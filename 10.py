with open("10.txt") as f:
    data = f.read().split("\n")[:-1]

def is_corrupt(line):
    stack = []
    def top_of_stack_matches(c):
        if len(stack) == 0:
            return False
        matching = {")":"(", "}":"{", "]":"[", ">":"<"}
        return stack[-1] == matching[c]
    for c in line:
        if c in ")}]>":
            if top_of_stack_matches(c):
                stack.pop()
            else:
                return c
        else:
            stack.append(c)
    return False

def resulting_stack(line):
    stack = []
    def top_of_stack_matches(c):
        if len(stack) == 0:
            return False
        matching = {")":"(", "}":"{", "]":"[", ">":"<"}
        return stack[-1] == matching[c]
    for c in line:
        if c in ")}]>":
            if top_of_stack_matches(c):
                stack.pop()
        else:
            stack.append(c)
    return stack

def to_complete(stack):
    matching = {"(":")", "{":"}", "[":"]", "<":">"}
    result = []
    while len(stack) > 0:
        result.append(matching[stack.pop()])
    return "".join(result)

def score_incomplete(completion):
    total = 0
    scores = {")":1, "]":2, "}":3, ">":4}
    for c in completion:
        total *= 5
        total += scores[c]
    return total

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

if __name__ == "__main__":
    total = 0
    incomplete_lines_scores = []
    for line in data:
        corrupt_char = is_corrupt(line)
        if corrupt_char:
            total += scores[corrupt_char]
        else:
            incomplete_lines_scores.append(score_incomplete(to_complete(resulting_stack(line))))
    print(total)
    incomplete_lines_scores.sort()
    print(incomplete_lines_scores[len(incomplete_lines_scores)//2])
