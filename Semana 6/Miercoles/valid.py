class Valid:
    def __init__(self, id, races):
        self.id = id
        self.list_races = races

    def start_valid(self):
        print(f"The valid {self.id} is starting...!")
        for race in self.list_races:
            race.start()
            race.choose_winner()