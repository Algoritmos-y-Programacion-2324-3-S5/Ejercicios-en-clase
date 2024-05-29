class Horse:
    def __init__(self, name_parameter, id):
        self.__name = name_parameter
        self.id = id

    def get_name(self):
        return self.__name