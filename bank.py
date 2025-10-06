# Ask the user for initial balance and deposit amount
initial_balance = float(input("Enter your initial balance: ₹"))
deposit_amount = float(input("Enter the deposit amount: ₹"))

# Calculate updated balance
updated_balance = initial_balance + deposit_amount

# Display updated balance
print(f"Updated balance after deposit: ₹{updated_balance:.2f}")