def validation():
    num = int(input("How many lines of star pattern do you want to create? Please put an integer number between 1 and "
                    "20. "))
    while num < 1 or num > 20:
        if num < 1:
            print("You entered too small number. Please put an integer number between 1 and 20. ")
        else:
            print("You entered too large number. Please put an integer number between 1 and 20. ")
        num = int(input(
            "How many lines of star pattern do you want to create? Please put an integer number between 1 and 20. "))
    return num


def print_pattern(line_num):
    for space_count in range(line_num):
        # Print the spaces
        for space in range(space_count):
            print(" ", end="")
        # num_of_stars = 5 - num_of_spaces
        # Print the stars
        for star in range(2 * (space_count + 1)):
            print("*", end='')
        print()


line_num = validation()
print_pattern(line_num)
