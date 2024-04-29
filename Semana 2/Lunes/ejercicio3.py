print("***** Welcome to Pizzeria Napoli *****")
main_option = input("Please enter your option:\n1-Vegetarian\n2-No Vegetaria\n->")
if main_option == "1":
    option_ingredient = input("Please enter your option:\n1-Pimiento\n2-Tofu\n->")
    if option_ingredient == "1":
        ing = "Pimiento"
    else:
        ing = "Tofu"
    print(f"The selected pizza is Vegetarian and have tomato, mozzarella and {ing}")
elif main_option == "2":
    option_ingredient = input("Please enter your option:\n1-Peperoni\n2-Jamon\n3-Salmon\n->")
    if option_ingredient == "1":
        ing = "Peperoni"
    elif option_ingredient == "2":
        ing = "Jamon"
    else:
        ing = "Salmon"
    print(f"The selected pizza is non Vegetarian and have tomato, mozzarella and {ing}")

else:
    print("Invalid option")