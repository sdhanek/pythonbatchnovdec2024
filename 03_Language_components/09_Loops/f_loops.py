"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""

import sys

i = 0
while i <= 7:
    i += 1
    print(i, end=" ")


print("\n importance of break")
i = 0
while i <= 7:
    i += 1
    if i != 2 and i % 2 == 0:
        break
    print(i, end=" ")


print("\n importance of continue")
i = 0
while i <= 7:
    i += 1
    if i != 2 and i % 2 == 0:
        continue
    print(i, end=" ")


print("\n importance of pass")
i = 0
while i <= 7:
    i += 1
    if i % 2 == 0:
        pass  # It acts as a placeholder
    print(i, end=" ")

def myfunc():
    pass

class Myclass:
    pass 


print("\nimportance of sys.exit")
i = 0
while i < 7:
    i += 1
    if i % 2 == 0:
        sys.exit(0)
    print(i, end=" ")


# exit code 0 - successful/normal termination
# exit code non-zero - abnormal termination
print("next statement")

# Assignment: Try these break, continue, pass, on a for loop example

# Using break in a for loop
print("\n break in for loop:")
for i in range(1, 11):  # Looping from 1 to 10
    if i == 5:  # The loop will break when i equals 5
        break
    print(f"{i} ", end="")

print("\ncontinue in for loop:")
for i in range(1, 11):  # Looping from 1 to 10
    if i == 5:  # The loop will skip printing when i equals 5
        continue
    print(f"{i} ", end="")

print("\n pass in for loop:")
for i in range(1, 11):  # Looping from 1 to 10
    if i == 5:  # pass will act as a placeholder when i equals 5
        pass
    print(f"{i} ", end="")

# Using sys.exit in a for loop
import sys
print("\nsys.exit in for loop:")
for i in range(1, 11):  # Looping from 1 to 10
    if i == 5:  # sys.exit will terminate the program when i equals 5
        sys.exit(0)
    print(f"{i} ", end="")

# The next statement won't be printed because sys.exit terminates the program
print("This statement will not be printed")