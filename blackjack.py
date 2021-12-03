# Blackjack

import random
# The PLANNING phase
# Dealer cards
dealer_cards = []
# Player cards
player_cards = []

# Deal the cards
# Dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X &", dealer_cards[1])

# Player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

# Display the cards

# Sum of Dealer Cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")
    
# Sum of Player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit? "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from there cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)

# Compare sums of the cards between Dealer V Player
    if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
    else:
            print("You win!")
if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins!")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You win!! 21")
        
    
if len(player_cards) == 5:
    print("You win!")
    print("Play Again?")
break

# If Player card sum is greater than 21 = BUST
# If Player card sum is less than 21 = Option Hit or Stay
# If Player option Stay compare sum of Dealer v Player
# If Player sum < 21 && > Dealer sum then Player wins!
# If Player sum < Dealer Sum then Player loses.
