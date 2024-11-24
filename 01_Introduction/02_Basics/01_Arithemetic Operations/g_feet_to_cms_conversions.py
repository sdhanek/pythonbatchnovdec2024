"""
Purpose: Feet to centimetres conversion
    1 feet = 12 inches
    1 inch = 2.54 centimetres
    
Algorithm:
            Step 1: Get feet values in runtime
            Step 2: compute from feet to cms
                    feet to inches, then 
                    inches to centimeters convension
            Step 3: Display the results

"""

# Step 1: Get feet value as input from the user
feet = float(input("Enter the value in feet: "))

# Step 2: Convert feet to inches
# 1 feet = 12 inches
inches = feet * 12

# Step 3: Convert inches to centimeters
# 1 inch = 2.54 centimeters
centimeters = inches * 2.54

# Step 4: Display the result
print(f"{feet} feet is equal to {centimeters} centimeters.")
