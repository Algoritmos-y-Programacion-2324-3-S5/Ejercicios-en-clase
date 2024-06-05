class Subject:
    def __init__(self,name, credits):
        self.name = name
        self.credits = credits

class PreSubject(Subject):
    def __init__(self, name, credits, department):
        super().__init__(name, credits)
        self.department = department

class PostSubject(Subject):
    def __init__(self, name, credits, diploma):
        super().__init__(name, credits)
        self.diploma = diploma
