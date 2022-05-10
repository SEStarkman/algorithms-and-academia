import itertools


digit_mapping = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

def letter_combinations(digits):
    # combos = []
    for i, digit in enumerate(digits):
        digits[i] = digit_mapping[digit]

    combos = list(itertools.product(*digits))

    for i, combo in enumerate(combos):
        combos[i] = ''.join(combo)

    return combos


if __name__ == '__main__':
    digits = [2, 3, 4]
    print(letter_combinations(digits))