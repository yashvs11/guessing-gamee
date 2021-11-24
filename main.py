#Guessing game version 1
#25/11/21
#yash singh 
import random 
#target is a variable that stores a random number from 1 to 100
target = random.randint(1,100)
#guess variable stores users guess number
guess = int(input("guess a number ? "))


if guess == target: #this weill check if the users number is as the target
  print("congratulation you got the number ")
elif guess <= target: #check wheather the users guess is less than the target
  print("your guess was too low")
elif guess >= target:#check wheather the users guess is greater than the target
  print("your guess was too high")
else: #in case something went wrong- shouldn't actually run
  print("something went wrong")

