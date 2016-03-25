#Made by Samir Gupta
import random 
#Used to generate random letter
import string #Used to get letter
lives = 2 #Number of lives player has
a = raw_input("Enter a Letter:")
#Get user input to test if the user guessed the letter right
answer = ""#Will be used to test if the player wants to play again
test = True#Used to test for valid input from play again
random_letter = random.choice(string.ascii_lowercase)#Randomly generated letter
#While the player still have lives
while(lives > 0):
    #If the player guessed the right anser
    if a == random_letter:
        #Display message that the player won
        print "You Win!"
        #Prompt player if they want to play again
        answer = raw_input("Play again? Y/N")
        test = True#Used to test for valid input, mostly used if times played > 1
        #While there is no valid input
        while(test):
            #If the player wants to play again
            if answer == "y" or answer =="Y":
                lives = 2#Player lives reset
                random_letter = random.choice(string.ascii_lowercase)
                #Choose random letter
                a = raw_input("Enter a letter:")
                test = False
                    
            elif answer =="N" or  answer =="n":
                print "Bye!"
                break
            else:
                answer = raw_input("Invalid Response. Please try again. Play Again? Y/N")    
    else:
        print "You have",lives," lives left."
        lives = lives -1
        a = raw_input("Try again.")
    
    if lives == 0:
        print "The letter was:",random_letter
        answer = raw_input("Play again? Y/N")
        test = True
        while(test):
            if answer == "y" or answer =="Y":
                lives = 2
                random_letter = random.choice(string.ascii_lowercase)
                a = raw_input("Enter a letter:")
                test = False
                    
            elif answer =="N" or  answer =="n":
                print "Bye!"
                test = False
                break
            else:
               answer = raw_input("Invalid Response. Please try again. Play Again? Y/N")    
                    