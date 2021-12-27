# STEP 1: ASK THE USER THE NUMBER
input_value = int(input('Enter a positive integer:'))
EPSILON_VALUE = 0.0001
# Validate
while input_value < 0:
    print('Please type a positive number.')
    input_value = int(input('Enter a positive integer:'))

# Step 2: compare
estimate_value = input_value

# Step 3 : Evaluate
goodness_value = (input_value / estimate_value) - estimate_value
goodness_value = abs(goodness_value)

# Step 4: While loop
while goodness_value > EPSILON_VALUE:
    estimate_value = (((input_value / estimate_value) + estimate_value) / 2)
    goodness_value = ((input_value / estimate_value) - estimate_value)
    goodness_value = abs(goodness_value)


print('Value of Square Root')
print(input_value, format(abs(estimate_value), '.3f'))


