 #!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable
Step 2: create a reverse string , from the given string, using string reversal
Step 3: compare both with a condition and decide

"""
test_string = input("Enter any string:")
print("test_string    :", test_string)

#reverse string
reverse_string = test_string[::-1]
print("reverse_string =", reverse_string)

print(test_string == reverse_string)

print("test_string == reverse_string:", test_string == reverse_string)


if test_string == reverse_string:
    print(test_string, "is palindrome")
else:
    print(test_string, "is NOT a palindrome")  

# Assignment: test if a given sentence is palindrome or not
# HINT: ignore the whitespace and check  

def is_palindrome(sentence):
    # Remove whitespace and convert to lowercase
    a = ''.join(sentence.split()).lower()
    # Check if the cleaned sentence reads the same backward
    b = a[::-1]
    return a == b

#  usage
example_sentence = "AmanaPlanacanalPanamA"
if is_palindrome(example_sentence):
    print(f'"{example_sentence}" is a palindrome.')
else:
    print(f'"{example_sentence}" is not a palindrome.')

