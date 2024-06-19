def exponential(base, exp):
    if exp <= 0:
        return 1
    return base * exponential(base, exp -1)

def search_in_list(lista,number, index=0):
    if lista[index] == number:
        return True
    elif len(lista) - 1 == index:
        return False
    return search_in_list(lista,number,index+1)
        
    

def main():
    print("*** WELCOME ***")
    option = int(input("Enter a option 1- Exponential / 2- Search:"))
    if option == 1:
        print(exponential(int(input("Please enter the base:")), int(input("Please enter exp:"))))
    elif option == 2:
        lista = [1,2,3,4,5,6,7,8,9,0]
        number = int(input("Please enter what number you are looking for:"))
        if search_in_list(lista,number):
            print(f"The number {number} is present")
        else: 
            print(f"The number {number} is not present")


main()