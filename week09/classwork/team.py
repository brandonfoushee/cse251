import random
import string
import sys
import time

# You might need to add this module by running (in a terminal): py -m pip install termcolor
from termcolor import colored

# TODO: Fix the recursive code so that it can find your house. Your house has a value of -2.

# Definitions:
# - A neighborhood is a two-dimensional array (2 x 2 grid) of integers. The size of neighborhood
#   is defined by the global SIZE variable.
# - An odd value is a house, an even value is a street (pathway through the neighborhood).
# - A house is a particular location in the neighborhood, so a coordinate (row, col).
# - Your house will always be in the last row at a random column (with a value of -2).

# Pseudocode (steps of how it works):
# 1. In recursive function, check if a house (row, col) in the neighborhood is your house
#    (equals -2). If it is, return True.
# 2. Determine if you have already checked this house (row, col): if True, return False
# 3. Add house to solution path (list)
# 4. Recursively check the next column and current row if house (row, next_col) is even
# 5. Recursively check the current column and next row if house (next_row, col) is even
# 6. If the recursive call returns True, return True again to exit; else remove
#    house from solution path


# Size of the neighborhood (SIZE x SIZE)
SIZE = 15

# Proven algorithm (so modify at your own discretion/peril)


def get_even_paths(row: int, col: int, neighborhood):
    even_paths = []
    # Move to the right, -1 indicates out of bounds
    next_col = col + 1 if col + 1 < SIZE else -1
    # Move down a row, -1 indicates out of bounds
    next_row = row + 1 if row + 1 < SIZE else -1

    # Is value in next column and current row even
    if next_col != -1 and neighborhood[row][next_col] % 2 == 0:
        #print(f'adding next_col: {row},{next_col}, value={map[row][next_col]}')
        even_paths.append((row, next_col))

    # Is value in current column and next row even
    if next_row != -1 and neighborhood[next_row][col] % 2 == 0:
        #print(f'adding next_row: {next_row},{col}, value={map[next_row][col]}')
        even_paths.append((next_row, col))

    return even_paths


# Make this function work
def find_house_recursively(neighborhood: list[list[int]], row: int, col: int, solution_path: list, complete_path: list) -> bool:

    # Determine if we have already checked this row and col
    if (row, col) in complete_path:
        print("already in path")
        return False

    # append house (row, col) to complete_path
    complete_path.append((row, col))

    # Check if this house is your house
    if neighborhood[row][col] == -2:
        print("found my house")
        return True

    # Create list to store any path that contains an even value
    even_paths = get_even_paths(row, col, neighborhood)

    # Now loop over each path and recursively check if it leads to your house
    for r, c in even_paths:

        # Add to path before checking if r and c are on the solution path since
        # if we find the house, we will return out of function
        solution_path.append((r, c))

        # If this r and c are the house, then exit by returning
        t = threading.Thread(find_house_recursively, args=(neighborhood, r, c, solution_path, complete_path))
        t.start()

        # Since we returned False from recursive call, we know we didn't find the house
        # so can remove the r and c from the solution path
        solution_path.remove((r, c))
    
    return False

# working print function


def printNeighborhood(neighborhood, path=None):

    for row in range(SIZE):
        for col in range(SIZE):
            alreadyPrintedValue = False
            if path != None:
                for r, c in path:
                    if r == row and c == col:
                        print(f"{colored(neighborhood[row][col], 'red')} ", end="")
                        alreadyPrintedValue = True
            if not alreadyPrintedValue:
                print(f"{colored(neighborhood[row][col], 'white')} ", end="")
        print()

#################################################################################
# Make sure to read through all lines of code, so you understand how this works #
#################################################################################
def find_house():

    # Create a SIZE x SIZE array (list of lists)
    neighborhood = [[0 for x in range(SIZE)] for y in range(SIZE)]

    # Fill in the neighborhoods with odd and even numbers.
    # The path to your house is along even numbers
    for row in range(1, SIZE):
        for col in range(1, SIZE):
            neighborhood[row][col] = (row * 2) // col

    # -2 is your house (bottom row, random column)
    neighborhood[SIZE - 1][random.choice([0, 1, 4, 6, 7, 8, 9])] = -2

    printNeighborhood(neighborhood)

    # The solution path from the start to the end
    solution_path = []

    # The complete path that each recursive call checks,
    # this is used to prevent checking the same square more
    # than once.
    complete_path = []

    # add the beginning house to the solution_path (upper left corner)
    solution_path.append((0, 0))
    find_house_recursively(neighborhood, 0, 0, solution_path, complete_path)

    print(f'{solution_path=}')

    # print map and color the path
    printNeighborhood(neighborhood, solution_path)


def main():
    # stop execution if too many recursive calls have been made
    sys.setrecursionlimit(5000)
    find_house()


if __name__ == "__main__":
    main()
