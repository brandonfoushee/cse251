import pickle
from MyClass import Person

with open('grade.dat', 'rb') as f:
    person1 = pickle.load(f)
    person2 = pickle.load(f)
    person3 = pickle.load(f)
    
    #print(f'\n{person1.name=}, {person1.grade=}')
    #print(f'{person2.name=}, {person2.grade=}')
    #print(f'{person3.name=}, {person3.grade=}')

    print(f'{person1}')
    print(f'{person2}')
    print(f'{person3}')
