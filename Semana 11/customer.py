class Customer:
    def __init__(self,name, age,dni, phone, people_quantity) -> None:
        self.name= name
        self.age= age
        self.dni= dni
        self.phone= phone
        self.people_quantity = people_quantity
        self.reservations = []