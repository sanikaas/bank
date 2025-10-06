# Ask the user for initial balance and deposit amount
initial_balance = float(input("Enter your initial balance: ₹"))
deposit_amount = float(input("Enter the deposit amount: ₹"))

# Calculate updated balance
updated_balance = initial_balance + deposit_amount

# Display updated balance
print(f"Updated balance after deposit: ₹{updated_balance:.2f}")

# Ask the user for initial balance and deposit amount
initial_balance = float(input("Enter your initial balance: ₹"))
deposit_amount = float(input("Enter the deposit amount: ₹"))

# Update balance after deposit
balance = initial_balance + deposit_amount
print(f"Updated balance after deposit: ₹{balance:.2f}")

# Ask user for withdrawal amount
withdraw_amount = float(input("Enter the withdrawal amount: ₹"))

# Check sufficient balance
if withdraw_amount > balance:
    print("Insufficient funds! Withdrawal denied.")
else:
    balance -= withdraw_amount
    print(f"Updated balance after withdrawal: ₹{balance:.2f}")
