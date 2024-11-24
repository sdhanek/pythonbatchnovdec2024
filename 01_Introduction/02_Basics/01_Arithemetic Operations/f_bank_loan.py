"""
Purpose: Bank Loan
Simple Interest = A = P (1 + rt)
                    A = final amount
                    P = initial principal balance
                    r = annual interest rate in percentage
                    t = time (in years)
                    n = Compounding frequency per year

Compound: P * (1 + r / n)^(n * t)
ref: https://www.calculatorsoup.com/calculators/financial/loan-calculator-simple.php

simple interest
compound interest
"""

P = 1500  # Principal amount
r = 5     # Annual interest rate in percentage
t = 3     # Time in years
n = 4     # Compounding frequency per year (quarterly)

# Convert interest rate to decimal
rate = r / 100

# Calculate Simple Interest
A_simple = P * (1 + rate * t)

# Calculate Compound Interest
A_compound = P * (1 + rate / n) ** (n * t)

print("Amount(SI):", A_simple)
print("Amount(CI):", A_compound)

A_simple = 1724.99
A_compound = 1741.13
