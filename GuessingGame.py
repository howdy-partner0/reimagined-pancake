
# generate random integer values
from random import seed
from random import randint

#computer generates a random number between 0 and 100
value = randint(0, 100)
#print(value)

i = 0
while i < 3:
    
    #asks user for a num between 0 and 100
    userInput = int(input("Guess a Number Between 0 and 100:\n"))
    
    #this if makes sure that the userinput is int and is between 0 and 100
    if isinstance(userInput, int) == True and userInput in range (1,100):
        
        if userInput == value:
            
	        print("You win")
	        
	        break
        elif userInput > value:
            
            print("The number is lower than the guess.\n")
            
        elif userInput < value:
            
            print("The number is higher than the guess.\n")
    
    else:
        print("Please enter a valid number")
        
    i +=1