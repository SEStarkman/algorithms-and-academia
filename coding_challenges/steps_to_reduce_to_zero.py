def number_of_steps(num):
    counter = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        counter += 1
    
    return counter


if __name__ == '__main__':
    num = 123
    print(number_of_steps(num))