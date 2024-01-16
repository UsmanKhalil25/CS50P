def calulate(expression):
    firstNumber,operation,secondNumber = expression.split(" ")
    if operation == "+":
        return float(firstNumber)+ float(secondNumber)
    elif operation == "-":
        return float(firstNumber)- float(secondNumber)
    elif operation == "*":
        return float(firstNumber)* float(secondNumber)
    elif operation == "/":
        return float(firstNumber)/ float(secondNumber)
    
def main():
    expression = input("Expression: ")
    print(calulate(expression))

main()