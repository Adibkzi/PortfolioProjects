print('Welcome to the Compound Interest Calculator.')
initial_amount = int(input("Please enter the initial amount of your investment:"))  # P
interest_rate = float(input('Please enter the interest rate:'))  # R
investment_year = int(input("Please enter the number of years for the investment:"))  # T
compound_year = int(input("Please enter the number of compounding per year:"))  # N

# MATH SECTION
original_investment = initial_amount
final_balance = initial_amount * (1 + (interest_rate * 1) / compound_year) ** (compound_year * investment_year)
interest_earned = original_investment + final_balance

# Calling
print(f"Original Investment:$", format(original_investment, ",.2f"))
print(f"Interest Earned:$", format(interest_earned, ",.2f"))
print(f"Final Balance:$", format(final_balance, ',.2f'))
