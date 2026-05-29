#!/usr/bin/env python3

# Author ID: bhodes

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    return int(number1) - int(number2)
    # Rememebr to make sure the function accepts 2 arguments

def multiply_numbers(number1, number2):
    return int(number1) * int(number2)
    # Remember to make sure the function accepts 2 argumrnts

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
