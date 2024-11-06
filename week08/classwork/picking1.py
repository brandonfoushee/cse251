import pickle
from MyClass import Person

person1 = Person("Aaron", 85)
person2 = Person("Brandon", 100)
person3 = Person("Becky", 50)

print(f'{person1}')

with open('grade.dat', 'wb') as f:
    b = pickle.dumps(person1)
    f.write(b)
    pickle.dump(person2, f)
    pickle.dump(person3, f)