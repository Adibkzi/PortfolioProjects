# Ask Player 1 for a number between 0 and 100
player_1 = int(input('Enter a number between 1 and 100.'))
# Next, have Player 2 guess what number was entered by Player 1
guess_number = -1
while guess_number != player_1:
    guess_number = int(input('Enter a guess'))
    if guess_number < player_1:
        print('Too low')
    elif guess_number > player_1:
        print('too high')
print('you got the right answer')
