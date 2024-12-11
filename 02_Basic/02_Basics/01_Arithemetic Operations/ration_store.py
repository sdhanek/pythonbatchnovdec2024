"""

Purpose: Ration store 
----------------------
Item    cost   quantity   Amount
Wheat   25/kg   30 kgs   25 * 30 = 750 /-
Rice    12/kg   50 kgs   12 * 50 = 600/-
                        -------------------
                                   1350/-
                        subsidy 20% -270/-
                        --------------------
                        Billable amount:1080/-


Algorithm  
---------
step 1 : get the cost of items into variables 
step 2 : get the quantity of items into variables
step 3 : compute the selling price to each item, and add them
step 4 : compute the subsidy amount and sutract from the selling price 
step 5 : Display the Billable Amount

"""
# Cost of items 
cost_of_wheat =25
cost_of_rice = 12
#Quantities of Items
qty_of_wheat = 30 # kgs
qty_of_rice = 50 #kgs

#selling price Computation 
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
#print(total_sp)
print("Total Selling Price:", total_sp)

# Subsidy Calculation at 20 % Subsidy
subsidy_amount = (total_sp * 20)/100 #PEMDAS
print ("Subsidy_amount:",subsidy_amount)

billable_amount = total_sp - subsidy_amount
print("Billable_Amount:", billable_amount)