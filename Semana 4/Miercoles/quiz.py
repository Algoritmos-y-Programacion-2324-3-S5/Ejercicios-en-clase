def show_welcome():
    print(" ***** Welcome to tech store *****")

def show_menu():
    option = input("Please enter a option: \n1-Show Inventory\n2-Purchase\n3-Exit\n->")
    return option

def show_inventory(inventory, inventory_option):
    option = ""
    if inventory_option == "1":
        option = "mobiles"
    elif inventory_option == "2":
        option = "laptops"  
    
    if option != "":
        for brand, product_list in inventory.get(option).items():
            print(brand)
            for product in product_list:
                for key, value in product.items():
                    if key == "id":
                        print()
                        print(f"{value}", end = " - ")
                    else:
                        print(f"{value}", end = " ")
            
    else:
        print("Invalid inventory option")
    



def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
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
        },
    }
    show_welcome()
    while True:
        option_value = show_menu()
        if option_value == "1":
            inventory_option = input("What do you want to see\n1-Mobiles\n2-Laptops\n->")
            show_inventory(products, inventory_option)
        elif option_value == "2":
            pass
        elif option_value == "3":
            print("Thank you for your visit")
            break
        else:
            print("Invalid option")

main()
