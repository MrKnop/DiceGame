''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  Name:       Matthew Knop
  Date:       2/22/17

Description:    Writing a dice game in python 3.5. This project is
                from Rich Thompson of The University of Arizona. This
                project spec came directly from the class he taught
                called ISTA130.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random

'''
Method:     print_scores
Purpose:    This method prints the current score of both players.
Parameters: name1 - String of the first players name.
            name2 - String of the second players name.
            score1 - Integer value of the first player's score.
            score2 - Integer value of the second player's score.
'''
def print_scores(name1, score1, name2, score2):
    print "\n-- SCORES\t%s: %d\t%s: %d --" % (name1, score1, name2, score2)


'''
Method:     checkforwinner
Purpose:    This method returns true if there is a winner and prints their name, otherwise returns false.
Parameters: name - String of the current player's name.
            score - Integer of the current player's score.
'''
def checkforwinner(name, score):
    if score >= 50:
        print "\t\tTHE WINNER IS: %s" % name
        return True
    return False


'''
Method:     roll_again
Purpose:    Asks current player if want to roll again.
Parameters: name - String of the current player's name.
            score - Integer of the current player's score.
'''
def roll_again(name, score):
    while True:  # Loop for asking user about rolling again.
        answer = raw_input('Roll again, %s?(Y/N): ' % name)
        if answer == 'y' or answer == 'Y':
            return True
        elif answer == 'n' or answer == 'N':
            return False
        else:
            print('I don\'t understand: "%s". Please enter "Y" or "N".')


'''
Method:     play_turn
Purpose:    Executes current player's turn.
Parameters: name - String of the current player's name.
            score - Integer of the current player's score.
'''
def play_turn(name, score):
    print("---------- %s's turn ----------") % name
    while roll_again(name,score) == True:
        dice_roll = random.randint(1,6)
        print("<<< %s rolls a %d >>>") % (name, dice_roll)
        if dice_roll == 1:
            print("\t!!!PIG! No points earned, sorry %s!!!") % name
            score = 0
            break
        elif dice_roll != 1:
            score += dice_roll
            print("\tPoints: %d") % score
        if checkforwinner(name,score) == True:
            break
    return score

# ---------------------------------------------------------------------------------------------
def main():
    seed_value = input('Enter a seed value: \n\n')

    print('PigDice')
    player_one = raw_input('Enter name for player 1: ')
    player_two = raw_input('Enter name for player 2: ')
    print('\tHello %s and %s, welcome to PigDice!') % (player_one, player_two)
    score_one = 0
    score_two = 0
    print_scores(player_one, score_one, player_two, score_two)
    while True:
        # Player 1's turn.
        score_one = play_turn(player_one, score_one)
        print_scores(player_one, score_one, player_two, score_two)
        if checkforwinner(player_one, score_one) == True:
            break

        #Player 2's turn.
        score_two = play_turn(player_two, score_two)
        print_scores(player_one, score_one, player_two, score_two)
        if checkforwinner(player_two, score_two) == True:
            break

if __name__ == '__main__':
    main()
