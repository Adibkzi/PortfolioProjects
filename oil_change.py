# Get the current mileage and the mileage at the last oil change.
current_mileage = int(input("Enter the car's current mileage: "))
last_change_mileage = int(input("Enter the mileage at the last oil change: "))
# Check to see if the numbers make sense
if current_mileage < last_change_mileage:
    print("The current mileage is less than the last oil change mileage.  You should re-check your numbers!")
else:
    # Calculate difference in mileage
    mileage_difference = current_mileage - last_change_mileage
    # Check the mileage difference
    if mileage_difference > 5000:
        # Tell the user it is time for an oil change.
        print("Time for an oil change!")
    else:
        # It isn't time for a change.  Tell the user how many miles are left to go.
        print("You can keep driving for another", format(5000 - mileage_difference,",d"), "miles.")

