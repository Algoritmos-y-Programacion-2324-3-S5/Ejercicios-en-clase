def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        }
    }
    customers_data = {}
    customer_counter = 0
    product_types = ["mobiles","laptops"]
    while (True):
        option = input("Please select an option: \n 1- See Inventory\n 2-Purchase \n 3-Apply Promo\n 4-Exit\n ->")
        if option == "1":
            product_type = input("Please select an option: \n M- Mobiles\n L-Laptops \n A-Accesories\n ->")
            product_desicion = ""
            if product_type.upper() == "M":
                product_desicion = "mobiles"
            elif product_type.upper() == "L":
                product_desicion = "laptops"
            else:
                product_desicion = "accessories"
            
            brand = products.get(product_desicion)
            
            for brand_name, brand_products in brand.items():
                print(brand_name,":")
                for product_item in brand_products:
                    print(f"Product: {product_item.get('id')} - {product_item.get('name')} -> {product_item.get('price')} ")

        elif option == "2":
            name = input("Please enter your name: ")
            last_name = input("Please enter your last name: ")
            dni = input("Please enter your dni: ")
            product_id = input("Please enter product id: ")
            customer = {}
            customer["name"] = name
            customer["last_name"] = last_name
            customer["dni"] = dni
            customer["product_id"] = product_id
            customers_data[customer_counter] = customer

            found = False
            total = 0

            for type in product_types:
                if(not found):
                    brand = products.get(type)
                    for brand_name, brand_products in brand.items():
                        if(not found):
                            for product_item in brand_products:
                                if product_item.get('id') == int(customer.get("product_id")):
                                    total += float(product_item.get('price'))
                                    found = True
                

            if found: 
                customer["total"] = total
                print("****** FACTURA ******")
                print("Name :", customer.get("name"))
                print("Last Name :", customer.get("last_name"))
                print("DNI :", customer.get("dni"))
                print("Total :", customer.get("total"))

                customer_counter += 1
            else:
                print("Product not found")
        elif option == "3":
            for type in product_types:
                brand = products.get(type)
            
                for brand_name, brand_products in brand.items():
                    for product_item in brand_products:
                        if str(product_item.get('name')).isalnum():
                            product_item['promo'] = True
            
            print(products)
                            

        else:
            break


main()
