Bill = float(input("Enter the total bill amount: "))
Tip_Percentage = float(input("Enter the tip percentage you would like to give (e.g., 15 for 15%): "))
Number_of_People = int(input("Enter the number of people to split the bill: "))
Tip_Amount = Bill * (Tip_Percentage / 100)
Total_Bill = Bill + Tip_Amount
Amount_Per_Person = Total_Bill / Number_of_People
print(f"Each person should pay: ${Amount_Per_Person:.2f}")
# Tip Calculator    