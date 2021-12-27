# Write a program that simulates drawing a playing card from a deck until we get
# the same card on back-to-back draws.
# The program should print the values of each card, and count the number of draws
# performed before the program stops.
import random
# Draws one playing card, prints the card to the console, and returns the card value.
def draw_card():
    # Simulate the drawing of a single card, starting with the suit.
    suit = random.choice(['Hearts', 'Diamonds', 'Spades', 'Clubs'])
    # We could also use randint...
    # suit_int_value = random.randint(1,4)
    # if suit_int_value == 1:
    #     suit = "Hearts"
    # elif suit_int_value == 2:
    #     suit = "Diamonds"
    # elif suit_int_value == 3:
    #     suit = "Spades"
    # elif suit_int_value == 4:
    #     suit = "Clubs"
    # Next simulate the card value
    card_value = random.randint(1,13)
    if card_value == 1:
        card_value = "Ace"
    elif card_value == 11:
        card_value = "Jack"
    elif card_value == 12:
        card_value = "Queen"
    elif card_value == 13:
        card_value = "King"
    # Combine the suit and value into an overall String representation of the playing card.
    card_as_a_string = str(card_value) + " of " + suit
    # Print the values to the screen and return the total.
    print(card_as_a_string)
    return card_as_a_string
# Draw cards until we get duplicate values in back-to-back draws.  Count the numberof draws.
def main():
    # Initialize the loop with the first draw.
    this_draw = draw_card()
    last_draw = None
    draw_count = 1
    # Repeat with a loop, draw cards until we get back-to-back draws with the same value.
    while this_draw != last_draw:
        # Store old value
        last_draw = this_draw
        # Then draw again.
        this_draw = draw_card()
        # Increment our counter
        draw_count += 1
    # Display the number of draws required.
    print("The program stopped after", draw_count, "draws.")
# Run the program!
main()