print("Greetings Players And Welocme To Arcadia")
Username = (input("What's Your Name: "))
print("\nHey",Username,"Welcome to Arcadia, A place for games based on RNG, Probability or Luck it's one and the same.\n \nWe provide you entertainment through games like Roll The Dice, Rock Paper Scissor, Blackjack and the likewise \nThanks for the visit and we hope you enjoy your stay in our humble abode\n ")
golden_drachma = 5000
stam = 100
print('\nYou are given',golden_drachma,'golden_drachmas and',stam,'Stamina for the start\n')
print ("\nEach game consumes some amout of stamina ,And you have to place a bet for each game for which if u win you are given different multipliers of your bet")
input()
import sys
import random
import time 
import os
def dotmsg(string):
    for i in string:
        print(i, end="")
        time.sleep(0.4)
                        
arcade = True 
while arcade :
        
        if golden_drachma == 0 : 
            arcade = False 
            break 
      
        if stam == 0 : 
            arcade == False 
            print("\nYou Ran Out Of Stamina")
            print("\nCome Back later")
            break 
        
        print("\nWhich Game You Wanna Play \tgolden_drachma:",golden_drachma,"\tStamina: ",stam,"\n 1. Roll The Dice \n 2. Rock Paper Scissors \n 3. Roulette \n 4. Blackjack \n 5. Shop \n 6. Leave")
        try:
            choice = int(input("Choose a game by it's number: "))
        except ValueError:
            print("Please Enter Valid Input")
            continue     
        while choice > 6 or choice < 1:
            choice = int(input("Please Enter Valid Input!"))
        
        if choice == 1 :
            q = True
            
            if stam < 5 :
                    print("\nNot Enough Stamina To Continue ")
                    break
            else :    
                print("In Roll The Dice you and the AI both will roll a dice and if the numbers match, you'll get twice the amount you bet and if you lose, the bet amount will be deducted from total amount.\nThis game will use up 5 stamina")
            
            while q:
                if stam == 0: 
                    break
                if stam < 5 :
                    print("\nNot Enough Stamina To Continue ")
                    break
                
                dice_reps = ("",
                 "  _ _ _ \n |     |\n |  .  |\n |_ _ _|\n ",
                 "  _ _ _ \n |     |\n | . . |\n |_ _ _|\n ",
                 "  _ _ _ \n |     |\n | ... |\n |_ _ _|\n ",
                 "  _ _ _ \n | . . |\n | . . |\n |_ _ _|\n ",
                 "  _ _ _ \n | . . |\n | .`. |\n |_ _ _|\n ",
                 "  _ _ _ \n | ... |\n | ... |\n |_ _ _|\n ")

                x = (input("\nAre you ready to Roll Some Dice? (Yes/No): ")).lower()
                if x == 'yes':
                    q = True
                    stam = stam - 5     
                    
                elif x == 'no':
                    break
                else:
                    print("Please Enter Valid Input!")
                    continue
                try:                 
                    bet = int(input("How much you wanna bet on your Win?: "))
                except ValueError:
                    print("Please Enter Valid Value!")
                    continue
                if bet > golden_drachma:
                    print("Please Bet Accourding To Your golden_drachma Value!")
                    print("You Have Only", golden_drachma, "golden_drachmas Left")
                    continue
                roll = int(input("Enter the value you would like to bet on (value should be More then 0 And Less then 7): "))
                if roll>6 or roll<1:
                    print("Please Enter Valid Value!")
                    continue
                
                
                print( "Rolling The Dice...")               
                print("The Value Is....")
                if __name__ == '__main__':
                    msg = ". . . . .\n"
                    dotmsg(msg)
                result = random.randint(1, 6)               
                print (dice_reps[result])
                print(result)
                if roll == result:
                    print("OHhh, Lucky You!!")
                    golden_drachma = golden_drachma + bet
                else:
                    print("Better Luck Next Time :P")
                    golden_drachma = golden_drachma - bet
                    


                print("golden_drachma Left :",golden_drachma)
                print("Stamina Left :",stam)
                if golden_drachma > 0:
                    continue 
                elif golden_drachma == 0:
                    print("\nGAME OVER!!!")
                    break 
            else:
                    print("\nWell See You Later Then",Username)
        
        
        elif choice == 2 :
            
            RPS = True 
            
            if stam < 10 :
                    print("\nNot Enough Stamina To Continue")
                    break
            else :
                print('Welcome to Rock Paper Scissors Fellow Player')
                print("\nWinning rules of The Rock Paper Scissors game as follows: \n"
                                +"Rock vs Paper -> Paper wins \n"
                                + "Rock vs Scissors -> Rock wins \n"
                                +"Paper vs Scissors -> Scissors wins \n"
                                + "If you Win you will get twice the amount you have bet \n"
                                + "If you Lose then the amount you have betted will be Deducted fomr your golden_drachmas \n"
                                + "If its a Tie No Change will happen in your golden_drachma nor your Stamina\n")
            while RPS:
                if stam == 0: 
                    break
                
                if stam < 10 :
                    print("\nNot Enough Stamina To Continue")
                    break
                
                x = (input("You ready to play some Rock Paper And Scissors? (Yes/No): ")).lower()
                if x == 'yes':
                    RPS = True
                    stam = stam - 10
                    
                elif x == 'no':
                    RPS = False
                    continue
                else:
                    print("Please Enter Valid Value!")
                    continue

                t = ['Rock','Paper','Scissors']
                cc = (random.choice(t))
                #cc is computer choice 

                try:                 
                    bet = int(input("How much you wanna bet on your Win?: "))
                except ValueError:
                    print("Please Enter Valid Value!")
                    continue
                if bet>golden_drachma:
                    print("Please Bet Accourding To Your golden_drachma Value!")
                    print("You Have Only", golden_drachma, "golden_drachmas Left")
                    continue
    
    
                print("\nEnter Your Choice \n Rock \n Paper \n Scissors \n")
                uc = input("Your Choice Is: ")
                #uc is user choice 

                while uc != 'rock' and uc != 'paper' and uc != 'scissors' and uc != "Scissors" and uc != 'Rock' and uc != 'Paper':
                    uc = input("Please Enter A Valid Choice! ")
    
                if uc == 'Rock' or uc == 'rock':
                    uc2 = 'R'
                elif uc == 'Paper' or uc == 'paper':
                    uc2 = 'P'
                elif uc == 'Scissors' or uc == 'scissors':
                    uc2 = 'S'
        
        
                print("\nComputer's Choice Is....")
                if __name__ == '__main__':
                    msg = ". . . . ."
                    dotmsg(msg)                
                print(cc) 
            
                #the real checking
    
                #u chose rock and ai does rock  - tie
                if cc == "Rock" and uc2 == 'R':
                    print("It Was A Tie!")
                    golden_drachma = golden_drachma 
                    stam = stam + 10
        
                #u chose paper and ai does rock - win
                elif cc == "Rock" and uc2 == 'P':
                    print("It Was A Win! :p")
                    golden_drachma = golden_drachma + (2*bet)
    
                #u chose scissors and ai does rock - lose 
                elif cc == "Rock" and uc2 == 'S':
                    print("It Was A Lose : ( ")
                    golden_drachma = golden_drachma - bet
    
                #u chose rock and ai does paper - lose
                elif cc == "Paper" and uc2 == 'R':
                    print("It Was A Lose : ( ")
                    golden_drachma = golden_drachma - bet  
    
                #u chose paper and ai does paper - tie 
                elif cc == "Paper" and uc2 == 'P':
                    print("It Was A Tie!")
                    golden_drachma = golden_drachma 
                    stam = stam + 10
    
                #u chose scissors and ai does paper - win 
                elif cc == "Paper" and uc2 == 'S':
                    print("It Was A Win! :p")
                    golden_drachma = golden_drachma + (2*bet)
        
                #u choose rock and ai does scissors - win 
                elif cc == "Scissors" and uc2 == 'R':
                    print("It Was A Win! :p")
                    golden_drachma = golden_drachma + (2*bet)
        
                #u choose paper and ai does scissors - lose 
                elif cc == "Scissors" and uc2 == 'P':
                    print("It Was A Lose : ( ")
                    golden_drachma = golden_drachma - bet
        
                #u choose scissors and ai does scissors - tie 
                elif cc == "Scissors" and uc2 == 'S':
                    print("It Was A Tie!")
                    golden_drachma = golden_drachma
                    stam = stam + 10
                            
                print("golden_drachma Left :",golden_drachma)
                print("Stamina Left :",stam)
                if golden_drachma > 0:
                    continue 
                elif golden_drachma == 0:
                    print("\nGAME OVER!!!")
                    break 
     
            else:
                print("\nWell see you later then",Username)
                    
        elif choice == 3:   
            r = True
            if stam < 5 :
                    print("\nNot Enough Stamina To Continue ")
                    break
            else :    
                #do what i wrote after intro plz , with all the shit and even decide the items in the shop all up to u what u want just have boba in it                
                print("Roulette is a casino game named after the French word meaning little wheel which was likely developed from the Italian game Biribi.\n" 
                        +"\nIn the game, a player may choose to place a bet on a single number, various groupings of numbers, the color red or black, whether the number is odd or even, or if the numbers are high (19–36) or low (1–18).\n"
                        +"\n This will cost you 20 stamina and if you win you'll get 10 times your bet and if you loose the amount you have bet will get deducted")
            while r:
    
                if stam == 0: 
                    break
                if stam < 20 :
                    print("\nNot Enough Stamina To Continue ")
                    break
       
                x = (input("You ready to play some roulette? (Yes/No): ")).lower()
                if x == 'yes':
                    r = True
                    stam = stam - 20
                elif x == 'no':
                    r = False
                    continue
                else:
                    print("please enter valid input!")
                    continue
                bet = int(input("Amount of money you wanna bet: "))
                
                if bet>golden_drachma:
                    print("Please bet accourding to your golden_drachma value!")
                    print("You have", golden_drachma, "golden_drachmas")
                    continue
    
                roulette = {1:'Red',2:'Black',3:'Red',4:'Black',5:'Red',6:'Black',7:'Red',
                            8:'Black',9:'Red',10:'Black',11:'Black',12:'Red',13:'Black',14:'Red',15:'Black',16:'Red',
                            17:'Black',18:'Red',19:'Red',20:'Black',21:'Red',22:'Black',23:'Red',24:'Black',25:'Red',
                            26:'Black',27:'Red',28:'Black',29:'Black',30:'Red',31:'Black',32:'Red',33:'Black',34:'Red',
                            35:'Black',36:'Red',}
                
                RB = [  [1,2,3,4,5,6,7,8,9,10,11,12],
                        [13,14,15,16,17,18,19,20,21,22,23,24],
                        [25,26,27,28,29,30,31,32,33,34,35,36]]
   
                print("\nWhich kinda bet you waana make\n1.Single Number\n2.Color\n3.Odd and Even\n4.Rows\n5.Columes\n6.Range\n7.Leave")
                choice =int(input("Enter Your Choice: ")) 
                if choice < 1 or choice > 6:
                    print("Please enter a valid intput")
                    continue 
    
                if choice == 1:
                    print("On which number you wanna place you bet from 1-36?")
                    try:
                        bets = int(input("Which Number do you want to choose: "))
                    except ValueError:
                        print("Please enter a valid input")
                    if bets < 1 or bets > 36 :
                        print("Please enter a vlaid input")
                        continue 
                    print("The Roulette Gonna Spin Now")
                    if __name__ == '__main__':
                        msg = ". . . . ."
                        dotmsg(msg)
                    number,color = random.choice(list(roulette.items()))
                    print("\nThe Ball Landed On:",number)
        
                    if bets == number :
                        print("\nWOOHOO You Won")
                        golden_drachma = golden_drachma + (bet*10)
                    else:
                        print("\nF Mate You Lost")
                        golden_drachma = golden_drachma - bet
         
                      
                if choice == 2:
                    print("On which color you wanna place your bet\n1.Red\n2.Black")
                    try:
                        bets = int(input("Enter Your Choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                    if bets < 1 or bets > 2:
                        print("Please enter a valid input")
                        continue 
                    print("The Roulette Gonna Spin Now")
                    if __name__ == '__main__':
                        msg = ". . . . ."
                        dotmsg(msg)
                    number,color = random.choice(list(roulette.items()))
                    print("\nThe Ball Landed On:",color)
        
                    if bets == 1:
                        if color == 'Red':
                            print("\nWOOHOO You Won")
                            golden_drachma = golden_drachma + (bet*2)   
                        else :
                            print("\nF Mate You Lost")
                            golden_drachma = golden_drachma - bet
                
                    if bets == 2:
                        if color == 'Black':
                            print("\nWOOHOO You Won")
                            golden_drachma = golden_drachma + (bet*2)   
                        else :
                            print("\nF Mate You Lost")
                            golden_drachma = golden_drachma - bet
                
        
                if choice == 3:
                    print("On which you wanna make your bet \n1.Odd\n2.Even")
                    try:
                        bets = int(input("Enter Your Choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                    if bets < 1 or bets > 2:
                        print("Please enter a valid input")
                        continue 
                    print("The Roulette Gonna Spin Now")
                    if __name__ == '__main__':
                        msg = ". . . . ."
                        dotmsg(msg)
                    number,color = random.choice(list(roulette.items()))
                    print("\nThe Ball Landed On:",number)
                    
                    if bets == 1:
                        if (number%2) == 0:
                            print("\nF Mate You Lost")
                            golden_drachma = golden_drachma - bet
                        else:
                            print("\nWOOHOO You Won")
                            golden_drachma = golden_drachma + (bet*2)
                    if bets == 2:
                        if (number%2) == 0:
                            print("\nWOOHOO You Won")
                            golden_drachma = golden_drachma + (bet*2) 
                        else:
                            print("\nF Mate You Lost")
                            golden_drachma = golden_drachma - bet                       
        
        
                if choice == 4:
                    print("On which Row you wana make your bet \n1.1st row [1,2,3,4,5,6,7,8,9,10,11,12]\n2.2nd row [12,14,15,16,17,18,19,20,21,22,23,24]\n3.3rd row [25,26,27,28,29,30,31,32,33,34,35,36]")
                    try:
                        bets = int(input("Enter Your Choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                    if bets < 1 or bets > 3:
                        print("Please enter a valid input")
                        continue 
                    print("The Roulette Gonna Spin Now")
                    if __name__ == '__main__':
                        msg = ". . . . ."
                        dotmsg(msg)
                    number,color = random.choice(list(roulette.items()))

                    for i, j in enumerate(RB):
                        for l, m in enumerate(j):
                            if RB[i][l] == number:
                                print("\nThe Ball Landed On: Row",i+1)
                                print(RB[i])
                                if bets == i+1:
                                    print("\nWOOHOO You Won")
                                    golden_drachma = golden_drachma + (bet*2.5)
                                else:
                                    print("\nF Mate You Lost")
                                    golden_drachma = golden_drachma - bet
    
                if choice == 5:
                    print("On which column you wanna bet on ?")
                    for i in range(12):
                        if i < 9:
                            print("Column", i+1, end='  ')
                        else:
                            print("Column", i+1, end=' ')
                    print()
                    for i in range(3):
                        for j in range(12):
                            if RB[i][j] < 10:
                                print("      ", RB[i][j], end='  ')
                            else:
                                print("      ", RB[i][j], end=' ')
                        print()
                    try:
                        bets = int(input("Enter Your Choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                        
                    if bets < 1 or bets > 12:
                        print("Please enter a valid input")
                        continue
                    print("The Roulette Gonna Spin Now")
                    if __name__ == '__main__':
                        msg = ". . . . ."
                        dotmsg(msg)
                    number,color = random.choice(list(roulette.items()))
        
                    for i, j in enumerate(RB):
                        for l, m in enumerate(j):
                            if RB[i][l] == number:
                                print("\nThe Ball Landed On: Column",l+1, end='\n')
                                for z in range(3):
                                    print(RB[z][l], " ")
                                    
                                if bets == l+1:
                                    print("\nWOOHOO You Won")
                                    golden_drachma = golden_drachma + (bet*2.5)
                                else:
                                    print("\nF Mate You Lost")
                                    golden_drachma = golden_drachma - bet
        
    
                if choice == 6:
                    print("On which range you wanna place your bet?\n1.1st range [1-18]\n2.2nd range [19-36]")
                    try:
                        bets = int(input("Enter Your Choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                    if bets < 1 or bets > 2:
                        print("Please enter a valid input")
                        continue
                    print("The Roulette Gonna Spin Now")
                    if __name__ == '__main__':
                        msg = ". . . . ."
                        dotmsg(msg)
                    number,color = random.choice(list(roulette.items()))
        
                    r1 = range(1,19)
                    r2 = range(19,37)

                    if number in r1:
                        print("\nThe Ball Landed On: Range[1-18]")
                    elif number in r2:
                        print("\nThe Ball Landed On: Range[19-36]")
                    else:
                        pass
                    
                    if bets == 1:
                        if number in r1:
                            print("\nWOOHOO You Won")
                            golden_drachma = golden_drachma + (bet*2)
                        else:
                            print("\nF Mate You Lost")
                            golden_drachma = golden_drachma - bet
        
                    if bets == 2:
                        if number in r2:
                            print("\nWOOHOO You Won")
                            golden_drachma = golden_drachma + (bet*2)
                        else:
                            print("\nF Mate You Lost")
                            golden_drachma = golden_drachma - bet
 
        
                if choice == 7 :
                        print("See you Later")
                        break 
    
    
                print("\ngolden_drachma Left :",golden_drachma)
                print("Stamina Left :",stam)
                if golden_drachma > 0:
                    continue 
                elif golden_drachma == 0:
                    print("\nGAME OVER!!!")
                    break 
            else:
                print("Well see you later then",Username)
                
        
        elif choice == 4:
            
            Blackjack = True 
            
            if stam < 20 :
                    print("\nNot Enough Stamina To Continue")
                    break
            else :
                print('Welcome to Blackjack')
                print("\nRules of Blackjack: \n"
                                +"Blackjack is usually played at a table of 2-7 players and uses one to eight 52-card decks. All number cards (2-10) score the value indicated on them. The face cards (Jack, Queen, King) score 10 points and Ace can either be treated as 1 or 11. \n"
                                +"\nAt the beginning of each round, all players place their bets in their betting positions - also known as ‘boxes’. After the bets have been placed, all players are dealt two cards face-up in front of their respective betting positions. The dealer receives two cards, one face-up and another face-down.\n"
                                +"\nStarting to the left of the dealer, each player is given a chance to draw more cards. The players can either ‘hit’ or ‘stand’. If the player calls out ‘HIT’, they are given an extra card. They can then either call out ‘HIT’ again, or ‘STAND’ if they do not wish to draw any more cards. The player can ‘HIT’ as many times as they wish, but have to aim not to ‘bust’ (exceed a total of 21). \n"
                                +"\nIf the player busts, they immediately lose their bet. \n"
                                +"\nAfter each player has played and either stood or busted, the dealer takes their turn. They can, again, either ‘HIT’ or ‘STAND’. If the dealer’s hand exceeds 21, all players who didn't bust win immediately - their bet is returned along with a matching amount from the dealer's bank.\n"
                                +"\nIf the dealer reaches a valid hand, the cards are totalled and each player’s hand is compared to the dealer’s. If the player scored higher than the dealer, they win. If the player ties with the dealer, the original bet is returned to the player. Otherwise, the player loses their bet.\n"                                
                                +"\nA perfect hand combines an ace with a 10, Jack, Queen or King and is known as a ‘Blackjack’.\n"
                                +"\nIf you Lose then the amount you have bet will be Deducted from your golden_drachmas \n"
                                +"\nIf its a Tie No Change will happen in your golden_drachma nor your Stamina\n")
                
            while Blackjack:
                if stam < 10 :
                    print("\nNot Enough Stamina To Continue")
                    break
                
                x = (input("You ready to play some Blackjack (Yes/No): ")).lower()
                if x == 'yes':
                    Blackjack = True
                    stam = stam - 20
                    
                elif x == 'no':
                    Blackjack = False
                    break
                else:
                    print("Please Enter Valid Value!")
                    continue
                
                bet = int(input("How much you wanna bet on your Win?: "))
                if bet>golden_drachma:
                    print("Please Bet Accourding To Your golden_drachma Value!")
                    print("You Have Only", golden_drachma, "golden_drachmas Left")
                    continue
                
                decks = input("Enter number of decks to use: ")
                #user chooses number of decks to use
                deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)
                #if decks not in (2,3,4,5,6,7,8,9,10,11,12,13,14):
                 #   print("Please enter a valid value!")
                  #  continue
                
                #initialize scores
                wins = 0
                losses = 0
    
                def deal (deck):
                    hand = []
                    for i in range (2):
                        random.shuffle(deck)
                        card = deck.pop()
                        if card == 11:card = "J"
                        if card == 12:card = "Q"
                        if card == 13:card = "K"
                        if card == 14:card = "A"
                        hand.append(card)
                    return hand
                
                def play_again():
                    again=input("Do you want to play again? (Y/N): ").lower()
                    global dealer_hand, player_hand, deck, quit, Blackjack
                    if again == "y":
                        dealer_hand = []
                        player_hand = []
                        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
                        game()
                    else:
                        print("\ngolden_drachma Left :",golden_drachma)
                        print("Stamina Left :",stam)
                        print("Bye!")
                        quit = True
                        Blackjack = False
                            
                
                def total(hand):
                    total = 0
                    for card in hand:
                        if card == "J" or card == "Q" or card == "K":
                            total+=10
                        elif card ==  "A":
                            if total >= 11: total+=1
                            else: total+=1
                        else: total+=card
                    return total
                
                def hit(hand):
                    card = deck.pop()
                    if card == 11:card = "J"
                    if card == 12:card = "Q"
                    if card == 13:card = "K"
                    if card == 14:card = "A"
                    hand.append(card)
                    return hand
                        
                def print_results(dealer_hand, player_hand):
                    print("\n WELCOME TO BLACKJACK! \n")
                    print("-"*30+"\n")
                    print("   WINS:    %s    LOSSES:   %s\n" %(wins,losses))
                    print("-"*30+"\n")
                    print("The dealer has a " +str(dealer_hand)+"for a total of" + str(total(dealer_hand)))
                    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

                def blackjack(dealer_hand, player_hand):
                    global wins, losses, golden_drachma
                    if total(player_hand) == 21:
                        print_results(dealer_hand, player_hand)
                        print("Congratulations! You gota a Blackjack!\n")
                        golden_drachma = golden_drachma + (bet*2)
                        wins += 1
                        play_again()
                    elif total(dealer_hand) == 21:
                        print_results(dealer_hand,player_hand)
                        print("Sorry, you lose. The dealer got a blackjack.\n")
                        golden_drachma = golden_drachma - bet
                        losses += 1
                        play_again()
                        
                def score(dealer_hand,player_hand):
                    #score function now updates to global win/loss variables
                    global wins,losses,golden_drachma
                    if total(player_hand) == 21:
                        print_results(dealer_hand,player_hand)
                        print("Congratulations! You got a Blackjack!\n")
                        golden_drachma = golden_drachma + (bet*2)
                        wins += 1
                    elif total(dealer_hand) == 21:
                        print_results(dealer_hand, player_hand)
                        print ("Sorry, you lose. The dealer got a blackjack.\n")
                        golden_drachma = golden_drachma - bet
                        losses += 1
                    elif total(player_hand) > 21:
                        print_results(dealer_hand, player_hand)
                        print ("Sorry. You busted. You lose.\n")
                        golden_drachma = golden_drachma - bet
                        losses += 1
                    elif total(dealer_hand) > 21:
                        print_results(dealer_hand, player_hand)
                        print ("Dealer busts. You win!\n")
                        golden_drachma = golden_drachma + (bet*2)
                        wins += 1
                    elif total(player_hand) < total(dealer_hand):
                        print_results(dealer_hand, player_hand)
                        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
                        golden_drachma = golden_drachma - bet
                        losses += 1 
                    elif total(player_hand) > total(dealer_hand):
                        print_results(dealer_hand, player_hand)
                        print ("Congratulations. Your score is higher than the dealer. You win\n")
                        golden_drachma = golden_drachma + (bet*2)
                        wins += 1
                    
                def game():
                    global wins,losses,golden_drachma,Blackjack, quit
                    choice = 0
                    print("\n    WELCOME TO BLACKJACK!\n")
                    print("-"*30+"\n")
                    print("   WINS:    %s    LOSSES:   %s\n" %(wins,losses))
                    print("-"*30+"\n")
                    dealer_hand = deal(deck)
                    player_hand = deal(deck)
                    print("The dealer is showing a " + str(dealer_hand[0]))
                    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
                    blackjack(dealer_hand, player_hand)
                    quit=False
                    while not quit:
                        choice = input("Do you want to [H]it, [S]tand or [Q]uit: ").lower()
                        if choice == 'h':
                            hit(player_hand)
                            print(player_hand)
                            print("Hand total: " + str(total(player_hand)))
                            if total(player_hand)>21:
                                print('You busted')
                                golden_drachma = golden_drachma - bet
                                losses += 1
                                play_again()
                                
                        elif choice=='s':
                            while total(dealer_hand)<17:
                                hit(dealer_hand)
                                print(dealer_hand)
                                if total(dealer_hand)>21:
                                    print('Dealer busts, you win!')
                                    golden_drachma = golden_drachma + (bet*2)
                                    wins += 1
                                    play_again()
                            score(dealer_hand,player_hand)
                            play_again()
                        elif choice == 'q':
                            print("Bye")
                            quit=True
                            Blackjack = False
                            break
                game()

            if golden_drachma>0:
                continue
            elif golden_drachma == 0:
                print("\nGAME OVER!!!")
                Blackjack = False
                break
            else:
                print("Well see you later then",Username)
        
        elif choice == 5:
            shop = True 
            print("\nWelcome to shop fellow player")
            while shop :
                x = (input("\nAre You Intrested To Buy Something? (Yes/No): ")).lower()
                if x == 'yes':
                    shop = True
                elif x == 'no':
                    shop = False
                    continue
                else :
                    print("Please Enter Valid Value!")
                    continue
                
                print("\nHere Is The Menu Of The Arcadia \n1)-----------$100----------Recovers 5  Stamina \n2)-----------$200----------Recovers 10 Stamina \n3)-----------$500----------Recovers 20 Stamina \n4)-----------$1000---------Recovers 40 Stamina \n5)-----------$2000---------Recovers 60 Stamina \n6)Leave \n")             
                order = int(input("Which Item You Wanna Buy:"))
                
                if order == 1 :
                    stam = stam + 5
                    golden_drachma = golden_drachma - 100
                    print("You have brought the 1st item and now your stamina is",stam)
                    if stam > 100 :
                        print("\nSorry But You Cant Go Over 100")
                        stam = stam - 5
                        golden_drachma = golden_drachma + 100
                        print("You Have",stam,"Stam Left Now,And Your Currency Has Been Refunded")
                    else :
                        continue 
                    
                    
                elif order == 2 :
                    stam = stam + 10
                    golden_drachma = golden_drachma - 200
                    print("You have brought the 2nd item and now your stamina is",stam)
                    if stam > 100 :
                        print("\nSorry But You Cant Go Over 100")
                        stam= stam - 10
                        golden_drachma =golden_drachma + 200
                        print("You Have",stam,"Stam Left Now,And Your Currency Has Been Refunded")
                    else :
                        continue                     
                    
                elif order == 3 :
                    stam = stam + 20
                    golden_drachma = golden_drachma - 500
                    print("You have brought the 3rd item and now your stamina is",stam)                     
                    if stam > 100 :
                        print("\nSorry But You Cant Go Over 100")
                        stam= stam - 20
                        golden_drachma =golden_drachma + 500
                        print("You Have",stam,"Stam Left Now,And Your Currency Has Been Refunded")
                    else :
                        continue                    
                    
                elif order == 4 :
                    stam = stam + 40
                    golden_drachma = golden_drachma - 1000
                    print("You have brought the 4th item and now your stamina is",stam)
                    if stam > 100 :
                        print("\nSorry But You Cant Go Over 100")
                        stam= stam - 40
                        golden_drachma =golden_drachma + 1000
                        print("You Have",stam,"Stam Left Now,And Your Currency Has Been Refunded")
                    else :
                        continue 
                    
                elif order == 5 :
                    stam = stam + 60
                    golden_drachma = golden_drachma - 2000
                    print("You have brought the 5th item and now your stamina is",stam)
                    if stam > 100 :
                        print("\nSorry But You Cant Go Over 100")
                        stam= stam - 60
                        golden_drachma =golden_drachma + 2000
                        print("You Have",stam,"Stam Left Now,And Your Currency Has Been Refunded")
                    else :
                        continue 
                          
                elif order == 6:
                    print("See You Later",Username)                    
               
                    
        elif choice == 6:
            print("Well see you later then",Username)
            break
