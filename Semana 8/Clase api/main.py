def main():
    archivo = open('archivo.txt','rb')
    datos = archivo.read()
    archivo.close()
    print(datos)

main()