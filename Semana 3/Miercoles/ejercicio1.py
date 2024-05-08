table = input("Please enter a table or Y to exit: ")

while table.isnumeric():
    table = int(table)
    for number in range( 1, 11):
        print(f"{table} x {number} = {table * number}")
    table = input("Please enter a table or Y to exit: ")

print("Bye!!")

