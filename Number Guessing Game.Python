#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THIS IS SIMPLE NUMBER GUESSING GAME IN PYTHON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IT CONSISTS OF 3 DIFFICULTIES, EASY, MEDIUM AND HARD. THE USER HAS TO GUESS A NUMBER BETWEEN 1 AND 100 IN A CERTAIN NUMBER OF ATTEMPTS BASED ON THE DIFFICULTY SELECTED. THE GAME ALSO ASKS THE USER IF THEY WANT TO PLAY AGAIN AFTER THE GAME ENDS.#

#~~~~~~~~~Main game loop~~~~~~~~~#
import random
# We start by importing the random module to generate a random number for the game. We then enter an infinite loop that will keep the game running until the user decides to exit. Inside the loop, we display a welcome message and prompt the user to select a difficulty level. Based on the user's choice, we set the number of attempts they will have to guess the number. We then generate a random number between 1 and 100 for the user to guess.
while True:
    print("\nWelcome to the Number Guessing Game")
    print("1. Easy\n2. Medium\n3. Hard")

    difficulty = input("Select difficulty: ")

    if difficulty == "1":
        attempts = 15
    elif difficulty == "2":
        attempts = 10
    elif difficulty == "3":
        attempts = 5
    else:
        print("Invalid choice")
        continue

    number = random.randint(1, 100)
    print(f"You have {attempts} attempts to guess the number between 1 and 100.")
# We then enter another loop that will continue until the user runs out of attempts or guesses the number correctly. Inside this loop, we prompt the user to enter their guess and compare it to the generated number. If the guess is too low, we print a message indicating that it's too low. If it's too high, we print a message indicating that it's too high. If the guess is correct, we print a congratulatory message and break out of the loop.    
    while attempts > 0:
        guess = int(input("Guess the number: "))
        attempts -= 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct! 🎉")
            break

        
   # If the user runs out of attempts without guessing the number, we print a message revealing the correct number.    
    if attempts == 0:
     print("sorry, you have used all your attempts. The number was " + str(number))
    wanna_play = input("do you want to play again? yes or no: ")

    if wanna_play == "yes":
        print("\n restarting the game...")
    else:
        print("thank you for playing! goodbye!")
        break
