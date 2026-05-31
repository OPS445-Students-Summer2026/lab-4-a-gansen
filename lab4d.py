#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input1: str) -> str:
    # Place code here - refer to function specifics in section below
    new_str = input1[0:5]
    return new_str

def last_seven(input1: str) -> str:
    # Place code here - refer to function specifics in section below
    new_str = input1[-7:]
    return new_str    

def middle_number(input1: int) -> str:
    # Place code here - refer to function specifics in section below
    new_str = str(input1)[1:3]
    return new_str

def first_three_last_three(input1: str, input2: str) -> str:
    # Place code here - refer to function specifics in section below
    first_part = input1[0:3]
    second_part = input2[-3:]
    new_str = first_part + second_part
    return new_str


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))