def main():
    lista = [6,5,3,1,8,7,2,4]
    for i in range(len(lista)):
        temp = i
        value = lista[i]
        j = i - 1
        while j >= 0 and value < lista[j]:
            lista[temp] = lista[j]
            lista[j] = value
            temp-=1
            j-=1
    print(lista)

main()