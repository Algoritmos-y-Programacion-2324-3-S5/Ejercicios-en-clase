class ComercialAnnouncement:
    def __init__(self, name, dni, section, title, body):
        self.name = name
        self.dni = dni 
        self.section = section
        self.title = title
        self.body = body

class ClassifiedAnnouncement:
    def __init__(self, price, date, days, kind):
        self.price = price
        self.date = date
        self.days = days
        self.kind = kind

class ClassifiedVehicleAnnouncement(ClassifiedAnnouncement):
    def __init__(self, price, date, days, brand, model, year, color ,km):
        super().__init__(price, date, days, "Vehiculo")
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.km = km

class ClassifiedHomeAnnouncement(ClassifiedAnnouncement):
    def __init__(self, price, date, days, m2, baths, rooms, parking_spaces, politic):
        super().__init__(price, date, days, "Vivienda")
        self.m2 = m2
        self.baths = baths
        self.rooms = rooms
        self.parking_spaces = parking_spaces
        self.politic = politic
