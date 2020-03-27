import random

# Init deck
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4

names = ['Allan', 'Michele', 'Adrian', 'Robert']

# Ask for player name
player_name = input("What's your name? ")
dealer_name = names[random.randint(0, len(names) - 1)]

# init players and dealer

player = {'name': player_name, 'card': [], 'chips': 2500}
dealer = {'name': dealer_name, 'card': [], }


#  Add the cards
def addHand(deck, player):
    handSum[player] = 0

    for x in deck:
        if x in ["J", 'K', "Q"]:
            handSum[player] += 10
        elif "A" == x:
            if handSum[player] + 11 > 21:
                handSum[player] += 1


            else:
                handSum[player] += 11
        else:
            handSum[player] += int(x)


# Verification for win

def verWin(handVal):
    if handVal > 21:
        return False
    else:
        return True


# Info player
print('Welcom, {}! You are playing against {} and start with {} chips'.format(player['name'], dealer['name'],
                                                                              player['chips']))

# Start game
running = input('Are you ready to play?(y/n) ')

while running[0].upper() == 'Y':



    random.shuffle(deck)
    #print(deck)

    # distribute the cards
    dealer['card'] = deck[0:2]
    player['card'] = deck[2:4]

    print("Dealer have: {} {} \nYou have: {} {}".format('x', str(dealer['card'][1]), str(player['card'][0]),
                                                        str(player['card'][1])))

    # set the sum of cards
    handSum = {'dealer': None, 'player': None}

    # add the first two cards
    addHand(dealer['card'], 'dealer')
    addHand(player['card'], 'player')

    # print initial hand value
    print("your hand value: " + str(handSum['player']))

    # ask for bet
    print('You have {} chips'.format(player['chips']))

    while True:
        bet = int(input('How much you want to bet? '))
        if player['chips'] - bet < 0:
            print("You cant bet more than you have chips")
            continue
        else:
            break

    # Next cards
    nextCard = 4  # next item from deck
    while True:
        wantCard = input("You want another card?(y/n) ")

        if wantCard[0].upper() == 'Y':
            player['card'].append(deck[nextCard])
            nextCard += 1
            print(', '.join(player['card']))
            addHand(player['card'], 'player')
            print('hand value ' + str(handSum['player']))
            if verWin(handSum['player']):
                continue
            else:
                break
        else:
            break

    if verWin(handSum['player']):
        print('Dealer turn')
        while True:
            if handSum['dealer'] < 17:
                if verWin(handSum['dealer']):

                    dealer['card'].append(deck[nextCard])
                    nextCard += 1
                    print('Dealer card: ', end=' ')
                    print(', '.join(dealer['card']))
                    addHand(dealer['card'], 'dealer')
                    print('value ' + str(handSum['dealer']))


                else:
                    print('Dealer card: ', end=' ')
                    print(', '.join(dealer['card']))
                    break
            else:

                break

        if handSum['dealer'] > handSum['player'] and handSum['dealer'] < 22:
            print("Dealer win with", end=' ')
            print(', '.join(dealer['card']))


            player['chips'] -= bet
        elif handSum['dealer'] == handSum['player']:
            print('TIE')
        elif handSum['player'] < 22:
            print('Player win')
            player['chips'] += bet

    else:
        print('Dealer win')
        print('Dealer card: ', end=' ')
        print(', '.join(dealer['card']))
        player['chips'] -= bet

    if player['chips'] <= 0:
        print('You lost all the chips goodbye')
        break

    # ask for next round
    nextround = input('You want continue to play {} ?(y/n) '.format(player['name']))
    if nextround[0].upper() == 'Y':
        print('=====================New Game==========================')
        continue
    else:
        break
