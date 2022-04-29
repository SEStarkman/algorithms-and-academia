def can_construct(ransom_note, magazine):
    magazine = list(magazine)
    for letter in ransom_note:
        if letter in magazine:
            magazine.remove(letter)
        else:
            return False
    
    return True


if __name__ == '__main__':
    ransom_note = "aa"
    magazine = "aba"
    print(can_construct(ransom_note, magazine))