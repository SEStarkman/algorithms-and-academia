def roman_to_integer(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0
    while i < len(s):
        next_index = i + 1
        if next_index != len(s):
            if romans[s[i]] < romans[s[i+1]]:
                total += (romans[s[i+1]] - romans[s[i]])
                i += 2
            else:
                total += romans[s[i]]
                i += 1
        else:
            total += romans[s[i]]
            break

    return total


if __name__ == '__main__':
    s = "XCII"
    print(roman_to_integer(s))