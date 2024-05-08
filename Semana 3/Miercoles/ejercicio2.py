height = int(input("Please enter a height: "))
aux = 1
for number in range(5):
    if aux == 1:
        print(aux)
    elif aux > 1:
        print(aux, end= " ")
        for number2 in range(number,0,-2):
            print(number2)
    aux += 2

