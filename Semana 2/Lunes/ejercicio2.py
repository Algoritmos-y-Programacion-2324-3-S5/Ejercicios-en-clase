number1 = input("Please enter first number: ")
number2 = input("Please enter second number: ")

if number1.isnumeric() and number2.isnumeric():
    number1 = int(number1)
    number2 = int(number2)

    if number2 != 0:
        print(f"Result: {number1/number2}") 
    else:
        print("ERROR")
else:
    print("Please enter valid info")