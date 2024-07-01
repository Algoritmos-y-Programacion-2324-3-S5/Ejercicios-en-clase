class Room:
    def __init__(self,beds, baths, price,name) -> None:
        self.name = name
        self.beds= beds
        self.baths= baths
        self.price= price

class Suite(Room):
    def __init__(self, baths, price, has_jacuzzi):
        super().__init__(3, baths, price,"Suite")
        self.has_jacuzzi = has_jacuzzi

class Double(Room):
    def __init__(self, baths, price, is_individual):
        super().__init__(2, baths, price,"Double")
        self.is_individual = is_individual

class Simple(Room):
    def __init__(self, baths, price, has_tv) -> None:
        super().__init__(1, baths, price,"Simple")
        self.has_tv = has_tv