number = int(input("Please enter a number: "))
aux = 2
if number >= 2:
    isPrime = True
    while aux < number:
        if number % aux == 0:
            isPrime = False
            break
        aux+=1
    if isPrime:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")
else:
    print(f"The number {number} is not prime")