
# Smart Bill Splitter
# A beginner Python project

print("=" * 35)
print("        SMART BILL SPLITTER")
print("=" * 35)

# Get user input
bill_amount = float(input("Bill amount (TL): "))
tip_percentage = float(input("Tip percentage: "))
people_count = int(input("Number of people: "))

# Calculate the tip
tip_amount = bill_amount * tip_percentage / 100

# Calculate the total bill
total_amount = bill_amount + tip_amount

# Calculate the payment per person
per_person = total_amount / people_count

# Display results
print("-" * 35)
print(f"Bill amount:  {bill_amount:.2f} TL")
print(f"Tip:          {tip_amount:.2f} TL")
print(f"Total amount: {total_amount:.2f} TL")
print(f"Per person:   {per_person:.2f} TL")
print("=" * 35)
print("Enjoy your meal!")
