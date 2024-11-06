

class Person:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def __str__(self):
        return (f'name={self.name}, grade={self.grade}')