import pickle

class Animal:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def get_name(self):
        return f"The animal's name is {self.name}"

with open('animal.dat', 'rb') as f:
    animal = pickle.load(f)
    print(animal.get_name())