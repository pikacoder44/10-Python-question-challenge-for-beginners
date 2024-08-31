# Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.

def reverse_num(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10+digit
        num //= 10

    return reversed_num

def convert_to_binary(decimal):
    remainder = 0
    quotient = decimal
    binary = 0
    while(quotient!=0):
        
        remainder = quotient%2
        quotient = int(quotient/2) #get quotient
        binary = (binary*10)+remainder
    print(f"Binary: {reverse_num(binary)}")

n = int(input("Enter a num: "))
convert_to_binary(n)
