# Three Card Poker
# Python 2.7

import sys

# Takes in a string of length two and evaluates the rank of the card
# Returns an integer representing the value of the rank of the card
# Ex. 'K' -> 13
def Card_Value (card_string):
    if card_string[0] == 'T':
        value_of_rank = 10
    elif card_string[0] == 'J':
        value_of_rank = 11
    elif card_string[0] == 'Q':
        value_of_rank = 12
    elif card_string[0] == 'K':
        value_of_rank = 13
    elif card_string[0] == 'A':
        value_of_rank = 14 # The Ace could also represent a 1 when checking if the hand is a straight
    else: # This means that the value of the first character in the string is the int value
        value_of_rank = int(card_string[0])
    return value_of_rank

# Takes in three strings of length two (represents a hand) and evaluates the strength of the hand (1.04 - 6.04)
# The tenths and hundredths decimal places represent the strength of the hand:
# Ex1. A pair of 4's is equal to 2.04
# Ex2. A pair of King's is equal to 2.13
# Returns a floating point number representing the highest strength of the hand (a higher float represents a stronger hand)
# Ex. 4d 4h 4s -> 5.04
def Hand_Value (card1, card2, card3):
    if IsStraightFlush(card1, card2, card3):
        return round(6 + 0.01 * HighCard(card1, card2, card3), 2) # Calls the round() function to prevent any decimal errors
    elif IsThreeOfAKind(card1, card2, card3):
        return round(5 + 0.01 * Card_Value(card1), 2)
    elif IsStraight(card1, card2, card3):
        return round(4 + 0.01 * HighCard(card1, card2, card3), 2)
    elif IsFlush(card1, card2, card3):
        return round(3 + 0.01 * FlushValue(card1, card2, card3), 2)
    elif IsPair(card1, card2, card3):
        return round(2 + 0.01 * PairCardsValue(card1, card2, card3), 2)
    else:
        return round(1 + 0.01 * HighCard(card1, card2, card3), 2)

# Takes in three strings of length two and checks if they have the same suit
# Returns true if all three cards share the same suit and false if they don't
# Ex. 2h 3h 4h -> True
def IsStraightFlush (card1, card2, card3):
    if IsFlush(card1, card2, card3) and IsStraight(card1, card2, card3):
        return True
    else:
        return False

# Takes in three strings of length two and checks if they all have the same card value
# Returns True only if all three of the cards have the same card value otherwise it returns False
# Ex. 4d 4h 4s -> True
def IsThreeOfAKind (card1, card2, card3):
    if card1[0] == card2[0] and card2[0] == card3[0]:
        return True
    else:
        return False

# Takes in three strings of length two and checks if they result in a straight
# Returns True only if all three of the cards make a straight otherwise it returns false
# Ex. 3d 4h 5s -> True
def IsStraight (card1, card2, card3):
    a = [Card_Value(card1), Card_Value(card2), Card_Value(card3)]
    a.sort()

    if a[0] + 1 == a[1] and a[1] + 1 == a[2]:
        return True
    else: # Checks if there is a straight when the player has an Ace by turning the default value of the Ace (14) to 1
        for i in a:
            if i == 14:
                i = 1
        a.sort()
        if a[0] + 1 == a[1] and a[1] + 1 == a[2]: # Check if the new value of the Ace results in a straight
            return True
        else:
            return False

# Takes in three strings of length two and checks if they make a flush
# Returns True only if all three of the cards have the same suit otherwise it returns False
# Ex. 3h 4h 5h -> True
def IsFlush (card1, card2, card3):
    if card1[1] == card2[1] and card2[1] == card3[1]:
        return True
    else:
        return False

# Takes in three strings of length two and checks if they are a pair
# Returns True only if two of the cards have the same rank otherwise it returns False
# Ex. 4d 4h Ks -> True
def IsPair(card1, card2, card3):
    if card1[0] == card2[0] and card1 != card3[0] \
            or card2[0] == card3[0] and card2[0] != card1[0] \
            or card1[0] == card3[0] and card1[0] != card2[0]:
        return True
    else:
        return False

# Takes in three strings of length two and finds the highest card value
# Returns the card value of the card with the highest rank
# Ex. Ah 4d 3c -> 14
def HighCard(card1, card2, card3):
    highest_card_value = Card_Value(card1)
    if Card_Value(card2) > highest_card_value:
        highest_card_value = Card_Value(card2)
    if Card_Value(card3) > highest_card_value:
        highest_card_value = Card_Value(card3)
    return highest_card_value

# Requirement: Pass in a hand with a pair
# Takes in a hand with a pair and finds the card value of the pair
# Returns the card value of the pair
# Ex. 4h 4d 9c -> 4
def PairCardsValue(card1, card2, card3):
    if card1[0] == card2[0]:
        return Card_Value(card1)
    elif card2[0] == card3[0]:
        return Card_Value(card2)
    else: # card1[0] == card3[0]
        return Card_Value(card1)
    
# Requirement: Pass in a hand with a flush
# Takes in a hand with a flush and assigns the value of the flush
# Returns the value of the flush in order of the highest cards
def FlushValue(card1, card2, card3):
    flush_value = 0
    arr = [Card_Value(card1), Card_Value(card2), Card_Value(card3)]
    arr.sort(reverse=True)
    flush_value += arr[0]
    flush_value += arr[1] * 0.01
    flush_value += arr[2] * 0.0001
    return flush_value

# Takes in our dataset (a list of dictionaries) and prints out the winner(s)
# Ex. 0 2c As 4d
#     1 Kd 5h 6c -> 2
#     2 Jc Jd 9s
def FindAndPrintWinner(list_of_dictionaries):
    number_of_winners = 1
    winner_hand_value = list_of_dictionaries[0]["value_of_hand"]
    winner_id = []
    winner_id.append(list_of_dictionaries[0]["id"])

    for dictionary in list_of_dictionaries:
        if dictionary["value_of_hand"] > winner_hand_value:
            number_of_winners = 1
            winner_id = []
            winner_id.append(dictionary["id"])
        elif dictionary["value_of_hand"] == winner_hand_value and dictionary["id"] not in winner_id:
            number_of_winners += 1
            winner_id.append(dictionary["id"])
    if number_of_winners == 1:
        print winner_id[0]
    else: # number_of_winners > 1
        print winner_id[0],
        i = iter(winner_id)
        next(i)
        for e in i:
            print e,
        print

# Takes in the input, removes the first line (the number of players) and creates a list of dictionaries to store the players, their cards and their card values
# Then it calls the function FindAndPrintWinner() which calculates the winner using the list of dictionaries and outputs it to the console
def main():

    s = sys.stdin.read()
    s = s.split('\n')

    s.pop(0)

    list = []

    for person in s:
        person = person.split()
        list.append({"id": person[0], "card1": person[1], "card2": person[2], "card3": person[3], "value_of_hand": 0})

    for player in list:
        player["value_of_hand"] = Hand_Value(player["card1"], player["card2"], player["card3"])

    FindAndPrintWinner(list)

if __name__ == "__main__":
    main()
