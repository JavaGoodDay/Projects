# Import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask the Computer a question: (press enter to quit) ")
    
    answers = random.randint(1,9)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ("Loveleh")
    
    elif answers == 2:
        print ("This is why I am number one")
    
    elif answers == 3:
        print ("Sorreh")
    
    elif answers == 4:
        print ("Are you confused?")
    
    elif answers == 5:
        print ("Nationwide Housing...Building Society!")
    
    elif answers == 6:
        print ("You are now number two")
    
    elif answers == 7:
        print ("I am not an Octopus, My Friend")
    
    elif answers == 8:
        print ("Screens Please")
        
    elif answers == 9:
        print ("My Friend, I hate you")