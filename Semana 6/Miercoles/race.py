import random

class Race:
    def __init__(self, id, horses):
        self.id = id
        self.list_horses = horses

    def start(self):
        print("Paaaaaaaaartidaaaaaa!! Salieron los competidores:")
        for horse in self.list_horses:
            print(horse.get_name())

    def choose_winner(self):
        winner = random.choice(self.list_horses)
        print(f"******* The winner is {winner.get_name()} *******")