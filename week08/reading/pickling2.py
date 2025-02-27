import pickle

with open('grade.dat', 'rb') as f:
    person1 = pickle.load(f)
    person2 = pickle.load(f)
    person3 = pickle.load(f)
    
    print(f'person1={person1}')
    print(f'person2={person2}')
    print(f'person3={person3}')

