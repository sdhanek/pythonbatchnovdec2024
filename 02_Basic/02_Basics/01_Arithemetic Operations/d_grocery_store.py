""" 
Algorithm

Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user (in run time)
NOTE: input()
        -> to get value in run-time
"""
# cost of items
cost_of_rice = 10 #per kg
cost_of_wheat = 34 # per kg

# Quantities of Items
qty_of_rice = input("Enter Qty. of Rice (in Kgs):")
qty_of_rice = float(qty_of_rice)
print("Qty of Rice :", qty_of_rice)

# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
sp_of_rice = float(sp_of_rice)
print("SP of Rice: ", sp_of_rice)