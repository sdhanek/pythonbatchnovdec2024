#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""

temp = input("Enter temperature): ").strip().lower()

if temp.endswith('c'):
    celsius = float(temp[:-1])
    fahrenheit = (celsius * 9/5) + 32
    print(f"{fahrenheit}F")
elif temp.endswith('f'):
    fahrenheit = float(temp[:-1])
    celsius = (fahrenheit - 32) * 5/9
    print(f"{celsius}C")
else:
    print("Invalid input. Please enter a valid temperature with 'C' or 'F'.")