'''
Requirements:
1. Create a class that extends the 'threading.Thread' class (see https://stackoverflow.com/questions/15526858/how-to-extend-a-class-in-python). This means that the class IS a thread. 
   Any objects instantiated using this class ARE threads.
2. Instantiate this thread class that computes the product of all numbers 
   between one and that number (exclusive)
3. COMMENT every line that you write yourself.

Things to consider:
a. How do you instantiate a class and pass in arguments (see https://realpython.com/lessons/instantiating-classes/)?
b. How do you start a thread object (see this week's reading)?
c. How will you wait until the thread is done (see this week's reading)?
d. How do you get the value an object's attribute (see https://datagy.io/python-print-objects-attributes/)?
'''

import threading
from cse251functions import *

###############################
# DO NOT USE YOUR OWN GLOBALS #
###############################

# TODO - Create a thread class, see this week's reading to learn how (delete this line and
# replace with your own description of the purpose of your class)


def main():
    # Instantiate your thread class and pass in 5 (delete this line).
    # Test (assert) if its product attribute is equal to 45 (delete this line).
    # Note: do no use 'yourThread' as the name of your thread object (delete this line).
    assert yourThread.product == 24, f'The product should equal 24 but instead was {
        yourThread.product}'

    # Repeat, passing in 10 (delete this line).
    assert yourThread.product == 362880, f'The product should equal 362880 but instead was {
        yourThread.product}'

    # Repeat, passing in 15 (delete this line).
    assert yourThread.product == 87178291200, f'The product should equal 87178291200 but instead was {
        yourThread.product}'


if __name__ == '__main__':
    main()
    print("DONE")
    create_signature_file()
