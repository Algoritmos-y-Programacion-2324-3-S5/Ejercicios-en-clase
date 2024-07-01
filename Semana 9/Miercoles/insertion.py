def main():
    lista = [6,5,3,1,8,7,2,4] # 1
    for i in range(len(lista)):# n
        temp = i #n
        value = lista[i]#n
        j = i - 1#n
        while j >= 0 and value < lista[j]:#n2
            lista[temp] = lista[j]#n2
            lista[j] = value #n2
            temp-=1#n2
            j-=1#n2
    print(lista)#1
#2+4n+5n2 = O(n2)
main()