def lineal_search(number, lista):
    for n in lista:
        if n == number:
            return number

def main():
    lista = [6,5,3,1,8,7,2,4]
    number = int(input("Please enter what number do you want to find: "))
    if lineal_search(number, lista):
        print(f"The number {number} is present")
    else: 
        print(f"The number {number} is not present")
main()