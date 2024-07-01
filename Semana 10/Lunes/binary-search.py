from selection import selection

def binary_search(number, lista):
    start = 0
    final = len(lista)
    middle = (start+final)//2
    if len(lista) < 2:
        if len(lista) > 0:
            if lista[0] == number:
                return number
            else:
                return None
    
    if number > lista[middle]:
        return binary_search(number,lista[middle:final])
    elif number < lista[middle]:
        return binary_search(number,lista[start:middle])
    else:
        return number

def main():
    lista = [6,5,3,1,8,7,2,4]
    selection(lista)
    
    number = int(input("Please enter what number do you want to find: "))
    if binary_search(number, lista):
        print(f"The number {number} is present")
    else: 
        print(f"The number {number} is not present")
main()