from customer import Customer
from reservation import Reservation
from room import Suite, Double, Simple

def isPrime(number, aux):
    if number > 1:
        if aux < 2:
            return True
        if number%aux == 0:
            return False
        return isPrime(number,aux-1)
    else:
        return False
    
def isAbundate(subtotal):
    return True
    
def register_customer(customers,customers_suites,customers_double,customers_simple):
    subtotal = 0
    discount = 0
    subtotal_suite= 0
    subtotal_simple= 0
    subtotal_doble= 0
    customer = Customer(
        input("Please enter the customer name: "),
        input("Please enter the customer age: "),
        input("Please enter the customer dni: "),
        input("Please enter the customer phone: "),
        input("Please enter the customer people quantity: ")
    )
    while True:
        room_option = input("Please enter what room do you want:\n1-Suite-100$\n2-Double-60$\n3-Simple-40$:\n->")
        quantity = int(input("Please enter how many rooms do you want:"))
        nights = int(input("Please enter how many nights do you want:"))
        room = None
        if room_option == "1":
            room = Suite(
                2,
                100,
                True
            )
        elif room_option == "2":
            room = Double(
                1,
                60,
                False
            )
        else:
            room = Simple(
                1,
                40,
                True
            )
        
        customer.reservations.append(
            Reservation(
                nights,
                room,
                quantity
            )
        )
        option_exit= input("Do you want to do another reservation:1- Yes, Another option- Exit")
        if option_exit != "1":
            break
    print("******* INVOICE ********")
    print("Name:", customer.name)
    print("Dni:", customer.dni)
    print("phone:", customer.phone)
    print("Age:", customer.age)
    for reservation in customer.reservations:
        print("Room: ",reservation.room.name)
        print("Nights",reservation.nights)
        print("Quantity",reservation.room_quantity)
        subtotal += reservation.room.price * reservation.room_quantity * reservation.nights
    if isPrime(int(customer.age),int(customer.age)-1):
        discount += subtotal*0.1
    if isAbundate(subtotal):
        discount += subtotal*0.1
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Total:" + subtotal - discount)
    return subtotal_suite, subtotal_doble, subtotal_simple
     


def main():
    while True:
        option = input("Please press 1 if you want to register a customer or anyother key to exit:")
        customers=[]
        customers_suites=[]
        customers_double=[]
        customers_simple=[]
        total_suite= 0
        total_simple= 0
        total_doble= 0
        if option == "1":
            subtotal_suite, subtotal_doble, subtotal_simple = register_customer(customers,customers_suites,customers_double,customers_simple)
            total_suite+= subtotal_suite
        else: 
            break
        print("The quantity of alocated customers is:",len(customers))
        print("The quantity of alocated in suites is:",len(customers_suites))
        print("The quantity of alocated in doubles is:",len(customers_double))
        print("The quantity of alocated in simples is:",len(customers_simple))


main()
