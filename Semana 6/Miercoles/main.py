from horse import Horse
from race import Race
from valid import Valid

def create_horses(horses):
    horses.append(Horse("Rayo Veloz",1))
    horses.append(Horse("Negro",2))
    horses.append(Horse("Lebron",3))
    horses.append(Horse("McQueen",4))
    horses.append(Horse("Speedy",5))
    horses.append(Horse("Francesco",6))

def create_races(races, horses,races_quantity):
    for i in range(races_quantity):
        races.append(Race(i+1,horses))

def create_valids(valids, races):
    valids.append(Valid(5,races))
    valids.append(Valid(6,races))

def main():
    horses = []
    races = []
    valids = []
    races_quantity = int(input("How many races do you want in each valid: "))
    create_horses(horses)
    create_races(races, horses, races_quantity)
    create_valids(valids,races)
    for valid in valids:
        valid.start_valid()

main()