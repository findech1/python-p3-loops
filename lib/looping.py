#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
     print(counter)
    counter -=1
  
print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    squared_lst = [x**2 for x in lst]
    return squared_lst

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        print(fizzbuzz(num))

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# Calling the function to print FizzBuzz sequence
fizzbuzz_printer()
