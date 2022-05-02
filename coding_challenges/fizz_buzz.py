# Problem: https://leetcode.com/problems/fizz-buzz/

def fizz_buzz(n):
    ans = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            ans.append('FizzBuzz')
        elif i % 5 == 0:
            ans.append('Buzz')
        elif i % 3 == 0:
            ans.append('Fizz')
        else:
            ans.append(i)
    
    return ans


if __name__ == '__main__':
    print(fizz_buzz(15))