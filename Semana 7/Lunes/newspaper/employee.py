import random

class Employee:
    def __init__(self, name, dni, section):
        self.name = name
        self.dni = dni 
        self.section = section

class Boss(Employee):
    def __init__(self, name, dni, section, writters):
        super().__init__(name, dni, section)
        self.writters = writters

    def supervise(self):
        print(f"Supervising:")
        for writter in self.writters:
            print(writter.name)

    def choice_publish(self, article_list):
        print("The pulished article is")
        article = random.choice(article_list)

class Writer(Employee):
    def __init__(self, name, dni, section):
        super().__init__(name, dni, section)
    
    def write(self):
        print("Writing... ")