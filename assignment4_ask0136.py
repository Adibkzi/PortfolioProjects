import random


# Deals a card. Values range from 1 to 10
def deal_card(card_deck):
    # create a logic with which you can draw a card from the card deck

    # you draw one card from card_deck and assign it to card_val
    card_val = random.choice(card_deck)

    # remove the drawn from card_deck
    card_deck.remove(card_val)

    return card_deck, card_val


# Handles the player's turn.  Returns the point value for the player's hand.
def get_player_score(card_deck):
    card_deck, hand_val = deal_card(card_deck)
    card_deck, temp_val = deal_card(card_deck)
    hand_val += temp_val

    print("The sum of the first two cards is:", hand_val)

    user_response = input("Do you want to take another card?: (Y/N)")

    # you should display the sum of the two cards
    hand_val += temp_val
    print("Your hand now has a total value of", hand_val)
    # then, ask users whether they want to get another card
    # user_response = input("Do you want to take another card?: (Y/N)")
    # if either the user is busted or the user wants to stop, then you need to stop
    while user_response == "Y" or user_response == "y":
        # Get the player's score.
        card_deck, temp_val = deal_card(card_deck)
        hand_val += temp_val
        # Once you got the player_score, you have to check whether the player got busted
        busted = 21
        if hand_val > busted:
            print("You busted with a total value of", hand_val, ".", sep="")
            return hand_val

        print('You have stopped taking more cards with a hand value of.', hand_val)

        # ask user whether he/she wants to play another game
        user_response = input("Do you want to take another card?: (Y/N)")

    # return the player's score
    return hand_val


# Handle's the dealer's turn.  Returns the point value for the player's hand.
def get_dealer_score():
    # Deals a card. Values range from 16 to 21
    hand_val = random.randint(16, 21)
    return hand_val


# The main function.  It repeatedly plays games of blackjack until the user decides to stop.
def main():
    # Prime the loop and start the first game.
    user_response = "Y"
    while user_response == "Y" or user_response == "y":
        # Set a card deck
        card = list(range(1, 11)) * 4
        # Get the player's score.
        player_score = get_player_score(card)
        # Once you got the player_score, you have to check whether the player got busted, whether player's score
        if player_score > 21:
            print('** YOU LOSE **')
        else:
            dealer_score = get_dealer_score()
            print('The dealer was dealt a hand with a value of', player_score)

            if dealer_score > 21 or dealer_score < player_score:
                print('** YOU WIN **')
            else:
                print('** YOU LOSE **')

            # ask user whether he/she wants to play another game
            user_response = input("Do you want to play another game?: (Y/N)")


# Call the main function to start the blackjack program.
main()
