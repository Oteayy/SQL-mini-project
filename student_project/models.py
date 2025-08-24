class Student:
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        
    def __str__(self):
        return f'{self.name} {self.surname}, rođen {self.birth_year}'