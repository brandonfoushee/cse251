

class Person:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def getName(self):
        return f"returning name from getName method: {self.name}"
        
    def __str__(self):
        return (f'name={self.name}, grade={self.grade}')