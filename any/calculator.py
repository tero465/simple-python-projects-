import time

def calculator(a, b, operation):
    if operation == '*':
        return a * b
    elif operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

def delay(n):
    time.sleep(n)

print("(* + - /)")
delay(1)

print('Please select * for multiplication \nPlease select + for addition \nPlease select - for subtraction \nPlease select / for division')
delay(2)

userInput = input('Please select the operation you want to perform: ')

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

result = calculator(a, b, userInput)
print(f"The result is: {result}")
