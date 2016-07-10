#note: Created and tested in Python 3.5. Results may vary in Python 2.x.

import random
from random import randint


#CLASSES

class ModCard:
        def __init__(self, name, value, desc):
                self.name = name
                self.value = value
                self.desc = desc

x2 = ModCard('x2', 0, 'multiply total by 2')
x3 = ModCard('x3', 0, 'multiply total by 3')
x2even = ModCard('x2even', 0, 'multiply even values by 2')
x2odd = ModCard('x2odd', 0, 'multiply odd values by 2')
x3even = ModCard('x3even', 0, 'multiply even values by 3')
x3odd = ModCard('x3odd', 0, 'multiply odd values by 3')

class ActionCard:
        def __init__(self, name, value):
                self.name = name
                self.value = value

two = ActionCard('2', 2)
three = ActionCard('3',3)
four = ActionCard('4',4)
five = ActionCard('5',5)
six = ActionCard('6',6)
seven = ActionCard('7',7)
eight = ActionCard('8',8)
nine = ActionCard('9',9)
ten = ActionCard('10',10)
eleven = ActionCard('11',11)
twelve = ActionCard('12',12)

class ConditionalCard:
        def __init__(self, name, value, desc):
                self.name = name
                self.value = value
                self.dec = desc
                
plus2coin = ConditionalCard('plus2coin', randint(2,12), 'plus 2 coins if rounds won')
plus3coin = ConditionalCard('plus3coin', randint(2,12), 'plus 3 coins if rounds won')
plus4coin = ConditionalCard('plus4coin', randint(2,12), 'plus 4 coins if rounds won')
plus1vp = ConditionalCard('plus1vp', randint(2,12), 'plus 1 victory point if rounds won')
        
class Deck:
        def __init__(self, name):
                self.name = name

ModDeck = Deck([x2.name,x3.name,x2even.name,x2odd.name,x3even.name,x3odd.name])
ActionDeck = Deck([two.name,three.name,four.name,five.name,six.name,seven.name,eight.name,nine.name,ten.name,eleven.name,twelve.name])
ConditionalDeck = Deck([plus2coin.name, plus3coin.name, plus4coin.name, plus1vp.name, plus1vp.name, plus1vp.name])

ModDeckNames = ModDeck.name
ActionDeckNames = ActionDeck.name
ConditionalDeckNames = ConditionalDeck.name

class DeckValue:
        def __init__(self,value):
                self.value = value

ModDeckValue = DeckValue([x2.value, x3.value, x2even.value, x2odd.value, x3even.value, x3odd.value])
ActionDeckValue = DeckValue([two.value,three.value,four.value,five.value,six.value,seven.value,eight.value,nine.value,ten.value,eleven.value,twelve.value])
ConditionalDeckValue = DeckValue ([plus2coin.value, plus3coin.value, plus4coin.value, plus1vp.value, plus1vp.value, plus1vp.value])

ModDeckValues = ModDeckValue.value
ActionDeckValues = ActionDeckValue.value
ConditionalDeckValues = ConditionalDeckValue.value

starting_deck_A = random.sample(ActionDeckNames,11)
starting_deck_B = random.sample(ActionDeckNames,11)
startingDeck = (starting_deck_A + starting_deck_B)


#EMPTY VARIABLES

rounds = 0

player_1_coins = 0
player_2_coins = 0

player_1_victoryPoints = 0
player_2_victoryPoints = 0

player_one_buy_victoryPoint_cards = []
player_two_buy_victoryPoint_cards = []

player_one_buy_mod_cards = []
player_two_buy_mod_cards = []

player_one_buy_conditional_cards = []
player_two_buy_conditional_cards = []


#STATS

player_one_total = 0
player_two_total = 0

def scoreAverage():
        print (player_1_name + ' average: ' + str(player_one_total/rounds))
        print (player_2_name + ' average: ' + str(player_two_total/rounds))


#FUNCTIONS

def player_one_name():
        global player_1_name
        player_1_name = input ('Player 1, what is your name? ')
        if player_1_name == '':
                print ('No name entered. Please try again.')
                player_one_name()

def player_two_name():
        global player_2_name
        player_2_name = input ('Player 2, what is your name? ')
        if player_2_name == '':
                print ('No name entered. Please try again.')
                player_two_name()

def player_one_startGame():
    draw_one = input (player_1_name + ', press Enter to see the cards you start with. ')
    print (player_1_name +', these are your cards.')

def player_two_startGame():
    draw_two = input (player_2_name + ', press Enter to see the cards you start with. ')
    print (player_2_name +', these are your cards.')

def player_one_startingDeck():
        global player_one_randomizeDeck
        player_one_randomizeDeck = random.sample(startingDeck,22)
        print (player_one_randomizeDeck)
  
def player_two_startingDeck():
        global player_two_randomizeDeck
        player_two_randomizeDeck = random.sample(startingDeck,22)
        print (player_two_randomizeDeck)
        
def player_one_pickfive():
        global player_one_pickFiveCards
        player_one_pickFiveCards = random.sample(player_one_randomizeDeck, 5)
        global player_one_pickFiveCards_Value
        player_one_pickFiveCards_Value = []
        for x in player_one_pickFiveCards:
            if x == '2':
                player_one_pickFiveCards_Value.append(two.value)
            if x == '3':
                player_one_pickFiveCards_Value.append(three.value)
            if x == '4':
                player_one_pickFiveCards_Value.append(four.value)
            if x == '5':
                player_one_pickFiveCards_Value.append(five.value)
            if x == '6':
                player_one_pickFiveCards_Value.append(six.value)
            if x == '7':
                player_one_pickFiveCards_Value.append(seven.value)
            if x == '8':
                player_one_pickFiveCards_Value.append(eight.value)
            if x == '9':
                player_one_pickFiveCards_Value.append(nine.value)
            if x == '10':
                player_one_pickFiveCards_Value.append(ten.value)
            if x == '11':
                player_one_pickFiveCards_Value.append(eleven.value)
            if x == '12':
                player_one_pickFiveCards_Value.append(twelve.value)
            if x == 'x2':
                player_one_pickFiveCards_Value.append(x2.value)
            if x == 'x3':
                player_one_pickFiveCards_Value.append(x3.value)
            if x == 'x2even':
                player_one_pickFiveCards_Value.append(x2even.value)
            if x == 'x3even':
                player_one_pickFiveCards_Value.append(x3even.value)
            if x == 'x2odd':
                player_one_pickFiveCards_Value.append(x2odd.value)
            if x == 'x3odd':
                player_one_pickFiveCards_Value.append(x3odd.value)
            if x == 'plus2coin':
                player_one_pickFiveCards_Value.append(plus2coin.value)
            if x == 'plus3coin':
                player_one_pickFiveCards_Value.append(plus3coin.value)
            if x == 'plus4coin':
                player_one_pickFiveCards_Value.append(plus4coin.value)
            if x == 'plus1vp':
                player_one_pickFiveCards_Value.append(plus1vp.value)
                
        print ('A:) ' + str(player_one_pickFiveCards[0]) + ', ' + 'B:) ' + str(player_one_pickFiveCards[1]) + ', ' + 'C:) ' + str(player_one_pickFiveCards[2]) + ', ' + 'D:) ' + str(player_one_pickFiveCards[3]) + ', ' + 'E:) ' + str(player_one_pickFiveCards[4])) 

def player_two_pickfive():
        global player_two_pickFiveCards
        player_two_pickFiveCards = random.sample(player_two_randomizeDeck, 5)
        global player_two_pickFiveCards_Value
        player_two_pickFiveCards_Value = []
        for x in player_two_pickFiveCards:
            if x == '2':
                player_two_pickFiveCards_Value.append(two.value)
            if x == '3':
                player_two_pickFiveCards_Value.append(three.value)
            if x == '4':
                player_two_pickFiveCards_Value.append(four.value)
            if x == '5':
                player_two_pickFiveCards_Value.append(five.value)
            if x == '6':
                player_two_pickFiveCards_Value.append(six.value)
            if x == '7':
                player_two_pickFiveCards_Value.append(seven.value)
            if x == '8':
                player_two_pickFiveCards_Value.append(eight.value)
            if x == '9':
                player_two_pickFiveCards_Value.append(nine.value)
            if x == '10':
                player_two_pickFiveCards_Value.append(ten.value)
            if x == '11':
                player_two_pickFiveCards_Value.append(eleven.value)
            if x == '12':
                player_two_pickFiveCards_Value.append(twelve.value)
            if x == 'x2':
                player_two_pickFiveCards_Value.append(x2.value)
            if x == 'x3':
                player_two_pickFiveCards_Value.append(x3.value)
            if x == 'x2even':
                player_two_pickFiveCards_Value.append(x2even.value)
            if x == 'x3even':
                player_two_pickFiveCards_Value.append(x3even.value)
            if x == 'x2odd':
                player_two_pickFiveCards_Value.append(x2odd.value)
            if x == 'x3odd':
                player_two_pickFiveCards_Value.append(x3odd.value)
            if x == 'plus2coin':
                player_two_pickFiveCards_Value.append(plus2coin.value)
            if x == 'plus3coin':
                player_two_pickFiveCards_Value.append(plus3coin.value)
            if x == 'plus4coin':
                player_two_pickFiveCards_Value.append(plus4coin.value)
            if x == 'plus1vp':
                player_two_pickFiveCards_Value.append(plus1vp.value)
        print ('A:) ' + str(player_two_pickFiveCards[0]) + ', ' + 'B:) ' + str(player_two_pickFiveCards[1]) + ', ' + 'C:) ' + str(player_two_pickFiveCards[2]) + ', ' + 'D:) ' + str(player_two_pickFiveCards[3]) + ', ' + 'E:) ' + str(player_two_pickFiveCards[4]))

def pick_five_player_one():
    global rounds
    rounds +=1
    pickfive = input (player_1_name + ', press Enter to draw five cards.' + '(rounds #' + str(rounds) + ')')
    print (player_1_name +', this is your hand.')
       
def pick_five_player_two():
    pickfive = input (player_2_name + ', press Enter to draw five cards.' + '(rounds #' + str(rounds) + ')')
    print (player_2_name +', this is your hand.')

def pick_three_player_one():
        global pickthree_player_one
        pickthree_player_one = input (player_1_name + ', choose 3 cards. ').lower()
 
def pick_three_player_two():
        global pickthree_player_two
        pickthree_player_two = input (player_2_name + ', choose 3 cards. ').lower()

def pick_three_math_player_one():
               global player_one_picks
               if 'x2' in player_one_three_choices and 'x2even' not in player_one_three_choices and 'x2odd' not in player_one_three_choices and 'x3even' not in player_one_three_choices and 'x3odd' not in player_one_three_choices:
                       player_one_picks =([sum(x for x in player_one_three_choices_Value)])
                       player_one_picks = int(''.join(map(str,player_one_picks)))
                       player_one_picks = player_one_picks*2
                       print ('Your total is: ' + str(player_one_picks))
               elif 'x3' in player_one_three_choices and 'x2even' not in player_one_three_choices and 'x2odd' not in player_one_three_choices and 'x3even' not in player_one_three_choices and 'x3odd' not in player_one_three_choices:
                       player_one_picks =([sum(x for x in player_one_three_choices_Value)])
                       player_one_picks = int(''.join(map(str,player_one_picks)))
                       player_one_picks = player_one_picks*3
                       print ('Your total is: ' + str(player_one_picks))
               elif 'x2even' in player_one_three_choices:
                       if 'x2' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)*2  + sum((x for x in player_one_three_choices_Value if x%2 != 0))])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*2
                               print ('Your total is: ' +str(player_one_picks))
                       elif 'x3' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)*2  + sum((x for x in player_one_three_choices_Value if x%2 != 0))])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*3
                               print ('Your total is: ' +str(player_one_picks))
                       else:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)*2  + sum((x for x in player_one_three_choices_Value if x%2 != 0))])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               print ('Your total is: ' +str(player_one_picks))
               elif 'x2odd' in player_one_three_choices:
                       if 'x2' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)  + sum((x for x in player_one_three_choices_Value if x%2 != 0))*2])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*2
                               print ('Your total is: ' +str(player_one_picks))
                       elif 'x3' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)  + sum((x for x in player_one_three_choices_Value if x%2 != 0))*2])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*3
                               print ('Your total is: ' +str(player_one_picks))
                       else:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0) + sum((x for x in player_one_three_choices_Value if x%2 != 0))*2])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               print ('Your total is: ' +str(player_one_picks))
               elif 'x3even' in player_one_three_choices:
                       if 'x2' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)*3  + sum((x for x in player_one_three_choices_Value if x%2 != 0))])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*2
                               print ('Your total is: ' +str(player_one_picks))
                       elif 'x3' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)*3  + sum((x for x in player_one_three_choices_Value if x%2 != 0))])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*3
                               print ('Your total is: ' +str(player_one_picks))
                       else:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)*3  + sum((x for x in player_one_three_choices_Value if x%2 != 0))])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               print ('Your total is: ' +str(player_one_picks))
               elif 'x3odd' in player_one_three_choices:
                       if 'x2' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)  + sum((x for x in player_one_three_choices_Value if x%2 != 0))*3])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*2
                               print ('Your total is: ' +str(player_one_picks))
                       elif 'x3' in player_one_three_choices:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0)  + sum((x for x in player_one_three_choices_Value if x%2 != 0))*3])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               player_one_picks = player_one_picks*3
                               print ('Your total is: ' +str(player_one_picks))
                       else:
                               player_one_picks =([sum(x for x in player_one_three_choices_Value if x%2 == 0) + sum((x for x in player_one_three_choices_Value if x%2 != 0))*3])
                               player_one_picks = int(''.join(map(str,player_one_picks)))
                               print ('Your total is: ' +str(player_one_picks))
               else:
                       player_one_picks =([sum(x for x in player_one_three_choices_Value)])
                       player_one_picks = int(''.join(map(str,player_one_picks)))
                       print ('Your total is: ' +str(player_one_picks))

def pick_three_math_player_two():
               global player_two_picks
               if 'x2' in player_two_three_choices and 'x2even' not in player_two_three_choices and 'x2odd' not in player_two_three_choices and 'x3even' not in player_two_three_choices and 'x3odd' not in player_two_three_choices:
                       player_two_picks =([sum(x for x in player_two_three_choices_Value)])
                       player_two_picks = int(''.join(map(str,player_two_picks)))
                       player_two_picks = player_two_picks*2
                       print ('Your total is: ' + str(player_two_picks))
               elif 'x3' in player_two_three_choices and 'x2even' not in player_two_three_choices and 'x2odd' not in player_two_three_choices and 'x3even' not in player_two_three_choices and 'x3odd' not in player_two_three_choices:
                       player_two_picks =([sum(x for x in player_two_three_choices_Value)])
                       player_two_picks = int(''.join(map(str,player_two_picks)))
                       player_two_picks = player_two_picks*3
                       print ('Your total is: ' + str(player_two_picks))
               elif 'x2even' in player_two_three_choices:
                       if 'x2' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)*2  + sum((x for x in player_two_three_choices_Value if x%2 != 0))])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*2
                               print ('Your total is: ' +str(player_two_picks))
                       elif 'x3' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)*2  + sum((x for x in player_two_three_choices_Value if x%2 != 0))])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*3
                               print ('Your total is: ' +str(player_two_picks))
                       else:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)*2  + sum((x for x in player_two_three_choices_Value if x%2 != 0))])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               print ('Your total is: ' +str(player_two_picks))
               elif 'x2odd' in player_two_three_choices:
                       if 'x2' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)  + sum((x for x in player_two_three_choices_Value if x%2 != 0))*2])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*2
                               print ('Your total is: ' +str(player_two_picks))
                       elif 'x3' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)  + sum((x for x in player_two_three_choices_Value if x%2 != 0))*2])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*3
                               print ('Your total is: ' +str(player_two_picks))
                       else:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0) + sum((x for x in player_two_three_choices_Value if x%2 != 0))*2])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               print ('Your total is: ' +str(player_two_picks))
               elif 'x3even' in player_two_three_choices:
                       if 'x2' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)*3  + sum((x for x in player_two_three_choices_Value if x%2 != 0))])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*2
                               print ('Your total is: ' +str(player_two_picks))
                       elif 'x3' in player_two_three_choices:
                               player_one_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)*3  + sum((x for x in player_two_three_choices_Value if x%2 != 0))])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*3
                               print ('Your total is: ' +str(player_two_picks))
                       else:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)*3  + sum((x for x in player_two_three_choices_Value if x%2 != 0))])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               print ('Your total is: ' +str(player_two_picks))
               elif 'x3odd' in player_two_three_choices:
                       if 'x2' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)  + sum((x for x in player_two_three_choices_Value if x%2 != 0))*3])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*2
                               print ('Your total is: ' +str(player_two_picks))
                       elif 'x3' in player_two_three_choices:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0)  + sum((x for x in player_two_three_choices_Value if x%2 != 0))*3])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               player_two_picks = player_two_picks*3
                               print ('Your total is: ' +str(player_two_picks))
                       else:
                               player_two_picks =([sum(x for x in player_two_three_choices_Value if x%2 == 0) + sum((x for x in player_two_three_choices_Value if x%2 != 0))*3])
                               player_two_picks = int(''.join(map(str,player_two_picks)))
                               print ('Your total is: ' +str(player_two_picks))
               else:
                       player_two_picks =([sum(x for x in player_two_three_choices_Value)])
                       player_two_picks = int(''.join(map(str,player_two_picks)))
                       print ('Your total is: ' +str(player_two_picks))

def pick_three_player_one_choice():
        if pickthree_player_one == 'abc' or pickthree_player_one == 'acb' or pickthree_player_one == 'bac' or pickthree_player_one == 'bca' or pickthree_player_one == 'cab' or pickthree_player_one == 'cba':
               global player_one_three_choices
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[0])
               player_one_three_choices.append(player_one_pickFiveCards[1])
               player_one_three_choices.append(player_one_pickFiveCards[2])
               global player_one_three_choices_Value
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[0])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[1])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[2])
               pick_three_math_player_one()
        elif pickthree_player_one == 'abd' or pickthree_player_one == 'adb' or pickthree_player_one == 'bad' or pickthree_player_one == 'bda' or pickthree_player_one == 'dab' or pickthree_player_one == 'dba':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[0])
               player_one_three_choices.append(player_one_pickFiveCards[1])
               player_one_three_choices.append(player_one_pickFiveCards[3])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[0])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[1])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[3])
               pick_three_math_player_one()
        elif pickthree_player_one == 'abe' or pickthree_player_one == 'aeb' or pickthree_player_one == 'bae' or pickthree_player_one == 'bea' or pickthree_player_one == 'eab' or pickthree_player_one == 'eba':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[0])
               player_one_three_choices.append(player_one_pickFiveCards[1])
               player_one_three_choices.append(player_one_pickFiveCards[4])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[0])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[1])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[4])
               pick_three_math_player_one()
        elif pickthree_player_one == 'acd' or pickthree_player_one == 'adc' or pickthree_player_one == 'cad' or pickthree_player_one == 'cda' or pickthree_player_one == 'dac' or pickthree_player_one == 'dca':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[0])
               player_one_three_choices.append(player_one_pickFiveCards[2])
               player_one_three_choices.append(player_one_pickFiveCards[3])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[0])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[2])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[3])
               pick_three_math_player_one()
        elif pickthree_player_one == 'ace' or pickthree_player_one == 'aec' or pickthree_player_one == 'cae' or pickthree_player_one == 'cea' or pickthree_player_one == 'eac' or pickthree_player_one == 'eca':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[0])
               player_one_three_choices.append(player_one_pickFiveCards[2])
               player_one_three_choices.append(player_one_pickFiveCards[4])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[0])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[2])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[4])
               pick_three_math_player_one()
        elif pickthree_player_one == 'ade' or pickthree_player_one == 'aed' or pickthree_player_one == 'dae' or pickthree_player_one == 'dea' or pickthree_player_one == 'ead' or pickthree_player_one == 'eda':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[0])
               player_one_three_choices.append(player_one_pickFiveCards[3])
               player_one_three_choices.append(player_one_pickFiveCards[4])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[0])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[3])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[4])
               pick_three_math_player_one()
        elif pickthree_player_one == 'bcd' or pickthree_player_one == 'bdc' or pickthree_player_one == 'cbd' or pickthree_player_one == 'cdb' or pickthree_player_one == 'dbc' or pickthree_player_one == 'dcb':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[1])
               player_one_three_choices.append(player_one_pickFiveCards[2])
               player_one_three_choices.append(player_one_pickFiveCards[3])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[1])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[2])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[3])
               pick_three_math_player_one()
        elif pickthree_player_one == 'bce' or pickthree_player_one == 'bec' or pickthree_player_one == 'cbe' or pickthree_player_one == 'ceb' or pickthree_player_one == 'ebc' or pickthree_player_one == 'ecb':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[1])
               player_one_three_choices.append(player_one_pickFiveCards[2])
               player_one_three_choices.append(player_one_pickFiveCards[4])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[1])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[2])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[4])
               pick_three_math_player_one()
        elif pickthree_player_one == 'bde' or pickthree_player_one == 'bed' or pickthree_player_one == 'dbe' or pickthree_player_one == 'deb' or pickthree_player_one == 'ebd' or pickthree_player_one == 'edb':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[1])
               player_one_three_choices.append(player_one_pickFiveCards[3])
               player_one_three_choices.append(player_one_pickFiveCards[4])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[1])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[3])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[4])
               pick_three_math_player_one()
        elif pickthree_player_one == 'cde' or pickthree_player_one == 'ced' or pickthree_player_one == 'dce' or pickthree_player_one == 'dec' or pickthree_player_one == 'ecd' or pickthree_player_one == 'edc':
               player_one_three_choices = []
               player_one_three_choices.append(player_one_pickFiveCards[2])
               player_one_three_choices.append(player_one_pickFiveCards[3])
               player_one_three_choices.append(player_one_pickFiveCards[4])
               player_one_three_choices_Value = []
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[2])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[3])
               player_one_three_choices_Value.append(player_one_pickFiveCards_Value[4])
               pick_three_math_player_one()

def pick_three_player_two_choice():
        if pickthree_player_two == 'abc' or pickthree_player_two == 'acb' or pickthree_player_two == 'bac' or pickthree_player_two == 'bca' or pickthree_player_two == 'cab' or pickthree_player_two == 'cba':
               global player_two_three_choices
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[0])
               player_two_three_choices.append(player_two_pickFiveCards[1])
               player_two_three_choices.append(player_two_pickFiveCards[2])
               global player_two_three_choices_Value
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[0])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[1])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[2])
               global player_two_picks
               pick_three_math_player_two()
        elif pickthree_player_two == 'abd' or pickthree_player_two == 'adb' or pickthree_player_two == 'bad' or pickthree_player_two == 'bda' or pickthree_player_two == 'dab' or pickthree_player_two == 'dba':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[0])
               player_two_three_choices.append(player_two_pickFiveCards[1])
               player_two_three_choices.append(player_two_pickFiveCards[3])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[0])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[1])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[3])
               pick_three_math_player_two()
        elif pickthree_player_two == 'abe' or pickthree_player_two == 'aeb' or pickthree_player_two == 'bae' or pickthree_player_two == 'bea' or pickthree_player_two == 'eab' or pickthree_player_two == 'eba':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[0])
               player_two_three_choices.append(player_two_pickFiveCards[1])
               player_two_three_choices.append(player_two_pickFiveCards[4])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[0])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[1])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[4])
               pick_three_math_player_two()
        elif pickthree_player_two == 'acd' or pickthree_player_two == 'adc' or pickthree_player_two == 'cad' or pickthree_player_two == 'cda' or pickthree_player_two == 'dac' or pickthree_player_two == 'dca':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[0])
               player_two_three_choices.append(player_two_pickFiveCards[2])
               player_two_three_choices.append(player_two_pickFiveCards[3])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[0])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[2])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[3])
               pick_three_math_player_two()
        elif pickthree_player_two == 'ace' or pickthree_player_two == 'aec' or pickthree_player_two == 'cae' or pickthree_player_two == 'cea' or pickthree_player_two == 'eac' or pickthree_player_two == 'eca':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[0])
               player_two_three_choices.append(player_two_pickFiveCards[2])
               player_two_three_choices.append(player_two_pickFiveCards[4])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[0])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[2])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[4])
               pick_three_math_player_two()
        elif pickthree_player_two == 'ade' or pickthree_player_two == 'aed' or pickthree_player_two == 'dae' or pickthree_player_two == 'dea' or pickthree_player_two == 'ead' or pickthree_player_two == 'eda':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[0])
               player_two_three_choices.append(player_two_pickFiveCards[3])
               player_two_three_choices.append(player_two_pickFiveCards[4])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[0])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[3])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[4])
               pick_three_math_player_two()
        elif pickthree_player_two == 'bcd' or pickthree_player_two == 'bdc' or pickthree_player_two == 'cbd' or pickthree_player_two == 'cdb' or pickthree_player_two == 'dbc' or pickthree_player_two == 'dcb':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[1])
               player_two_three_choices.append(player_two_pickFiveCards[2])
               player_two_three_choices.append(player_two_pickFiveCards[3])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[1])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[2])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[3])
               pick_three_math_player_two()
        elif pickthree_player_two == 'bce' or pickthree_player_two == 'bec' or pickthree_player_two == 'cbe' or pickthree_player_two == 'ceb' or pickthree_player_two == 'ebc' or pickthree_player_two == 'ecb':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[1])
               player_two_three_choices.append(player_two_pickFiveCards[2])
               player_two_three_choices.append(player_two_pickFiveCards[4])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[1])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[2])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[4])
               pick_three_math_player_two()
        elif pickthree_player_two == 'bde' or pickthree_player_two == 'bed' or pickthree_player_two == 'dbe' or pickthree_player_two == 'deb' or pickthree_player_two == 'ebd' or pickthree_player_two == 'edb':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[1])
               player_two_three_choices.append(player_two_pickFiveCards[3])
               player_two_three_choices.append(player_two_pickFiveCards[4])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[1])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[3])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[4])
               pick_three_math_player_two()
        elif pickthree_player_two == 'cde' or pickthree_player_two == 'ced' or pickthree_player_two == 'dce' or pickthree_player_two == 'dec' or pickthree_player_two == 'ecd' or pickthree_player_two == 'edc':
               player_two_three_choices = []
               player_two_three_choices.append(player_two_pickFiveCards[2])
               player_two_three_choices.append(player_two_pickFiveCards[3])
               player_two_three_choices.append(player_two_pickFiveCards[4])
               player_two_three_choices_Value = []
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[2])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[3])
               player_two_three_choices_Value.append(player_two_pickFiveCards_Value[4])
               pick_three_math_player_two()

def continue_game():
        pick_five_player_one()
        player_one_pickfive()
        pick_three_player_one()
        pick_three_player_one_choice()

        pick_five_player_two()
        player_two_pickfive()
        pick_three_player_two()
        pick_three_player_two_choice()

def total_score_update():
    global player_one_total
    global player_two_total
    player_one_total += player_one_picks
    player_two_total += player_two_picks
    print (player_1_name + ', your total score is: ' + str(player_one_total))
    print (player_2_name + ', your total score is: ' + str(player_two_total))

def exceptions():
        print ('You did not choose two sets of three values to compare.  Each player must select a combination of three letters, not spaced.  Please try again.')
        continue_game()        


#GAME LOOP

player_one_name()
player_two_name()
player_one_startGame()
player_one_startingDeck()
player_two_startGame()
player_two_startingDeck()

while (player_1_victoryPoints <2 and player_2_victoryPoints <2):
        continue_game()

        try:
                if player_one_picks > player_two_picks:
                        player_1_coins +=2
                        total_score_update()
                        if 'plus2coin' in player_one_three_choices:
                                player_1_coins +=2
                        if 'plus3coin' in player_one_three_choices:
                                player_1_coins +=3
                        if 'plus4coin' in player_one_three_choices:
                                player_1_coins +=4
                        if 'plus1vp' in player_one_three_choices:
                                player_1_victoryPoints +=1
                elif player_two_picks > player_one_picks:
                        player_2_coins +=2
                        total_score_update()
                        if 'plus2coin' in player_two_three_choices:
                                player_2_coins +=2
                        if 'plus3coin' in player_two_three_choices:
                                player_2_coins +=3
                        if 'plus4coin' in player_two_three_choices:
                                player_2_coins +=4
                        if 'plus1vp' in player_two_three_choices:
                                player_2_victoryPoints +=1
                elif player_one_picks == 0 and player_two_picks == 0:
                        exceptions()
                        
                else:
                        continue_game()
        except:
                exceptions()

        print (player_1_name + ' has ' + str(player_1_coins) + ' coins.')
        print (player_2_name + ' has ' + str(player_2_coins) + ' coins.')

        if player_1_coins >= 6:
                player_one_buy_victoryPoint_cards = input (player_1_name + ', do you want to buy a Victory Point? y/n ').lower()

        if player_one_buy_victoryPoint_cards == 'y':
                player_1_victoryPoints += 1
                player_1_coins -=6
                player_one_buy_victoryPoint_cards = 'n'

        if player_1_coins >= 2:
                player_one_buy_mod_cards = input (player_1_name + ', do you want to buy a Mod Card? y/n ').lower()

        if player_one_buy_mod_cards == 'y':
                player_one_randomizeDeck.append(random.choice(ModDeckNames))
                player_1_coins -=2
                player_one_buy_mod_cards = 'n'
                print (player_1_name +', a Mod Card has been added to your deck.')
                print (player_one_randomizeDeck)

        if player_1_coins >= 2:
                player_one_buy_conditional_cards = input (player_1_name + ', do you want to buy a Conditional Card? y/n ').lower()

        if player_one_buy_conditional_cards == 'y':
                player_one_randomizeDeck.append(random.choice(ConditionalDeckNames))
                player_1_coins -=2
                player_one_buy_conditional_cards = 'n'
                print (player_1_name +', a Conditional Card has been added to your deck.')
                print (player_one_randomizeDeck)
                
        if player_2_coins >= 6:
                player_two_buy_victoryPoint_cards = input (player_2_name + ', do you want to buy a Victory Point? y/n ').lower()

        if player_two_buy_victoryPoint_cards == 'y':
                player_2_victoryPoints += 1
                player_2_coins -=6
                player_two_buy_victoryPoint_cards = 'n'

        if player_2_coins >= 2:
                player_two_buy_mod_cards = input (player_2_name + ', do you want to buy a Mod Card? y/n ').lower()

        if player_two_buy_mod_cards == 'y':
                player_two_randomizeDeck.append(random.choice(ModDeckNames))
                player_2_coins -=2
                player_two_buy_mod_cards = 'n'
                print (player_2_name +', a Mod Card has been added to your deck.')
                print (player_two_randomizeDeck)

        if player_2_coins >= 2:
                player_two_buy_conditional_cards = input (player_2_name + ', do you want to buy a Conditional Card? y/n ').lower()

        if player_two_buy_conditional_cards == 'y':
                player_two_randomizeDeck.append(random.choice(ConditionalDeckNames))
                player_2_coins -=2
                player_two_buy_conditional_cards = 'n'
                print (player_2_name +', a Conditional Card has been added to your deck.')
                print (player_two_randomizeDeck)
                
        print (player_1_name + ' has ' + str(player_1_victoryPoints) + ' victory points.')
        print (player_2_name + ' has ' + str(player_2_victoryPoints) + ' victory points.')
        
else:
        if player_1_victoryPoints == 2:  #this number can be increased or decreased depending on how long a game you want.
                print ('GAME OVER. ' + player_1_name + ' wins.')
                scoreAverage()
        else:
                print ('GAME OVER. ' + player_2_name + ' wins.')
                scoreAverage()


#STUFF TO FIX:

#combining between (x2 and x3) and (x2even and x3 even)
#ties = +/1 VP?, one-time use cards?
#finish game stats
#ONLINE MULTIPLAYER FUNCTIONALITY



