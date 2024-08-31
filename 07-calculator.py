# Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

# The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.

def calculator(operand1=0,operator="",operand2=0):
    if(operator=="+"):
        return operand1+operand2
    if(operator=="-"):
        return operand1-operand2
    if(operator=="*"):
        return operand1*operand2
    if(operator=="/"):
        return operand1/operand2
    else:
        return -1


op1 = int(input("Enter the first number: "))
op2 = int(input("Enter the second number: "))
print("Now you have to specify the operator:")
print("+ - * /")
operator = str(input("-> "))
print(calculator(op1,operator,op2))