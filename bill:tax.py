bill = float(input("Enter the Bill Amount: "))
People = int(input("Enter the Number of People: "))
sales_tax = 0.0825
tip_rate = 0.15

tax = bill * sales_tax

total_bill = bill + tax
tip = total_bill * tip_rate
total_bill += tip
amount_per_person = total_bill / People
print(f"Each person should pay: ${amount_per_person:.2f}")
