# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. 

# For example, if the function gets sent “4444444444444444”, then it should return “4444”.
def reverse_num(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10+digit
        num //= 10

    return reversed_num
def last(num):
    a = int(num/10)
    a=a*10
    finl=num-a
    return finl

def hide_cdno(number):
    last_four = 0
    
    extracted_num =0
    remaining= number
    i=0
    while(i<4):
        extracted_num= last(number)
        last_four=(last_four*10)+extracted_num
        number=int(number/10)
        remaining = int(remaining/10)
        i+=1
    
    print("Hidden Number: ",end="")
    print("*"*len(str(remaining))+str(reverse_num(last_four)))
n= int(input("Enter your bank account number: "))

hide_cdno(n)

