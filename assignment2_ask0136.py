# COMPOUND INTEREST CALCULATOR
print("Thank you for using the Compound Interest Calculator")
# ENTER INITIAL AMOUNT
initial_amount = int(input("Please enter the initial amount of the investment:"))

# ENTER THE INTEREST RATE
interest_rate = float(input("Please enter the interest rate(example: '.05' for 5% interest):"))

# ENTER THE NUMBER OF YEARS OF INVESTMENT
number_years = int(input("Please enter the number of years for how long you want the investment to be:"))

# ENTER THE COMPOUND YEARS
compound_years = int(input("Please enter the number of compounding per year:"))

# CALCULATION OF THE EQUATIONS`
final_balance = initial_amount * (1 + ((interest_rate * 1) / compound_years)) ** (compound_years * number_years)
interest_earned = (final_balance - initial_amount)

# FINAL RESULT OF EQUATION AND DISPLAY RESULT
print(f"Original Investment:$", format(initial_amount, ',.2f'))
print(f"Interest Earned:$", format(interest_earned, ',.2f'))
print(f"Final Balance:$", format(final_balance, ',.2f'))


