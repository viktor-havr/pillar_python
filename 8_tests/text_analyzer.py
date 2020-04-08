"""Analyzes a text file and computes metrics"""


def analyze_text(filename):
    lines = 0
    chars = 0
    spaces = 0
    with open(filename, mode='rt', encoding='utf-8') as file:
        for line in file:
            lines += 1
            chars += len(line)
            for char in line:
                if char == ' ':
                    spaces += 1
        return lines, chars, spaces
