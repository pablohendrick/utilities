# List Of Values
monthly_bills = []

# Values Of Bills
for i in range(12):
    value_bill = float (input(f"Enter the account amount of {i+1}/12: "))
    monthly_bills.append (value_bill)

# Calculate the total annual expenses
total_expenses = sum (monthly_bills)

# Print The Annual Values
print(f"Monthly Bills: {monthly_bills}")
print(f"Total Annual Expenses: {total_expenses}")
