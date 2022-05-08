def remove_duplicates(s, k):
    is_duplicate = False

    letters = set(s)

    letter_list = []
    for letter in letters:
        letter_list.append(letter*k)


    while not is_duplicate:
        none_left = 0
        for chunk in letter_list:
            if chunk in s:
                s = "".join(s.split(chunk))
            else:
                none_left += 1
        if none_left == len(letter_list):
            is_duplicate = True

    return(s)


if __name__ == '__main__':
    s = "pbbcggttciiippooaais"
    k = 2

    print(remove_duplicates(s, k))