name = input("Enter the product name: ")
price = float(input("Enter the product price: "))
quantity = int(input("Enter the product quantity: "))

print("The product is: {product} {precio:6.2f} {cantidad:3d} {total:8.2f}".format(product = name, precio = price, cantidad = quantity, total = price * quantity))
