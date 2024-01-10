from random import *     
from string import *
from time import *
user_pass=input("Enter your passward:")   #input from user
guess=""
passward=ascii_letters+digits

Attempts=0    # keep track of the number of attempts made to guess the user-provided password.
Start=time()  # capture the time before the password guessing 
while(guess!=user_pass):
    guess=""
    for letter in range(len(user_pass)):
        guess_letter=passward[randint(0,61)]
        guess=(guess_letter)+(guess)
        Attempts+=1
        print(guess)      # printing guessed passward
End=time() # capture the time after the password guessing 
print(f"Passward:{guess}")
print(f"Attempts:{Attempts}")
print(f"Time Taken:{End-Start :.2f} seconds")