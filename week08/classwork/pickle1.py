import pickle

class Animal:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def get_name(self):
        return f"The animal's name is {self.name}"

animal = Animal("Lion", 10)
with open('animal.dat', 'wb') as f:
    pickle.dump(animal, f)