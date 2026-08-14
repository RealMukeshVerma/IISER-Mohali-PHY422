import numpy as np
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    binary = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num = decimal_num // 2 
    return binary
decimal_num = int(input("Enter decimal number:"))
result = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is: {result}")
