"""
Algorithm
----
Step 0: declare the constants
Step 1: Get the cost of fruits into variables
Step 2: Get the quantity of fruits into variables.
Compute the end quantity, by substituting dozen value.
Step 3: Compute the selling price to each item,
and add them
Step 4: Compute the discount amount and subtract
from the selling price, to create payable amount
Step 5: Calculate GST amount and Add to payable amount,
to create billable amount
"""
# constants
DOZEN = 12
DISCOUNT = 2/100
GST = 12.5

# cost of fruits
cost_of_apple = 12 # per piece
cost_of_mango = 34 # per piece

# Quantities of fruits
qty_of_apples = 5 * DOZEN # pieces
qty_of_mangos = 3 * DOZEN # pieces

# Selling Price Computation - PEMDAS
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos
print("Total Selling Price :", total_sp)

# Discount Calculation
discount_amount = total_sp * DISCOUNT
print("Discount Amount:", discount_amount)

# Payable Amount Calculation
payable_amount = total_sp - discount_amount
print("Payable Amount:", payable_amount)

# GST Calculation - PEMDAS
gst_on_fruits = payable_amount * GST / 100
print("GST on Fruits:", gst_on_fruits)

# Billable Amount Calculation
billable_amount = payable_amount + gst_on_fruits
print ("Billable Amount:", billable_amount)