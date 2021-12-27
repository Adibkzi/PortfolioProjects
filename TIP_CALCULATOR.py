total_amount = float(input("Please enter the total amount of the bill:"))
tip_percentage = float(input("Please enter the tip percentage:"))
tip = total_amount * tip_percentage / 100
# Display the tip amount
print("Your tip is",(format(tip,".2f")))