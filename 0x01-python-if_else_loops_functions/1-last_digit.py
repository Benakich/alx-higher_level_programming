#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10
print("Last digit of {:d} is {:d}".format(number, last_digit), end=' and is ')
if last_digit > 5:
    print("{}".format("greater than 5"))
elif last_digit == 0:
    print("{}".format("0"))
else:
    print("{}".format("less that 6 and not 0"))
