#Write a function that prints the numbers from 1 to n. But for multiples of 3, print ‘Fizz’ instead of the number, and for multiples of 5, print ‘Buzz’. For numbers that are multiples of both 3 and 5, print ‘FizzBuzz’

# Sample output:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11

def fizzy(n):
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 5 == 0:
            print(f'{x} Fizzbuzz')
        elif x % 3 == 0:
            print(f'{x} Fizz')
        elif x % 5 == 0:
            print(f'{x} Buzz')
        else:
            print(x)

fizzy(15)