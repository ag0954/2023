#HW1b- Number guessing game
#Abraham Gutierrez
#CSCI 3412 002
#Sung-Hee Nam

#The purpose of this program is to design and build a number guessing game,
#a simple timer function, another guessing game, and Top 'n' number of words



#-------------------------------------Guessing Game----------------------------------------
#This part of the program is responsible for for the first guessing game
#It will generate a random interger number between 1,1000.
#Next, a binary search function will automatically guess the random number
#Then, it will compute the total and average amount of guesses out of 10k and 1m
#Finally, it will print out the previous values


#import files
import random

# Guessing game class
class guessingGame:
    #constructor for class
    #note: high(limit of range), max_tries(limit for amount of guesses)
    def __init__(self, high, max_tries):
        self.low = 1
        self.high = high
        self.max_tries = max_tries
        self.guesses = 0
        self.guesses_total = []
    #Function for binary search
    #takes the random number, and lowest & highest number in range
    #stores attempts
    def number_guess(self,x,low,high):
        attempts = 0
        #while our lowest limit is less or equal to our upper limut
        #divide each sample size by half until we find our random number
        while low<=high:
            mid = low + (high -low)//2
            # if the middle matches the random number
            if mid == x:
                return attempts
            #if our middle number is less than the random random
            elif mid < x:
                low = mid + 1
                attempts += 1
            #or our number is greater than x 
            else:
                high = mid - 1
                attempts += 1
    #This function calls the number_guess function using a random interger, lower limit, upper limit
    #It adds every try to a counter and appends each to try to a list of total amount of tries
    def guessing_game(self):
        #continues until we reach the max amount of tries allowed
        for x in range(self.max_tries):
            #call binary search and adds attempts to tries
            tries = self.number_guess(random.randint(self.low,self.high),0,self.high)
            self.guesses += tries
            self.guesses_total.append(tries)
        #finds the average of all the guessed numbers by the total amount of tries
        average = sum(self.guesses_total) / len(self.guesses_total)
        #print the values of total amount of guess and the average of all the guesses
        print(f"The random numbers betweeen 1 .. {self.max_tries}: Total guesses:{self.guesses} Avg:{average}\n")

game1 = guessingGame(1000,10000)
game1.guessing_game() 
game2 = guessingGame(1000000,10000)
game2.guessing_game()

#---------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------Simple timer function-------------------------------------------

#import time
import time
class simpleTimer:
    #constructer for simpleTimer
    def __init__(self,maxPrimes):
        self.maxPrimes = maxPrimes

    def listofPrimes(maxPrimes):


    def timeEfficiency(self):
        starTime = time.time()
        self.maxPrimes(self.maxPrimes)
        endTime = time.time()

        totalTime = endTime - starTime

        print(f"Start Time:{starTime}\nEnd Time:{endTime}\nTime Efficiency:{totalTime}")

