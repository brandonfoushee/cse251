import pickle
from MyClass import Person

person1 = Person("Brandon", 100)
person2 = Person("Aaron", 50)
person3 = Person("Andrea", 75)

with open('grade.dat', 'wb') as f:
    b = pickle.dumps(person1)
    f.write(b)
    b = pickle.dumps(person2)
    f.write(b)
    b = pickle.dumps(person3)
    f.write(b)