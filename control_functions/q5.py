print('''5. Number Guessing Game
Beginner
Concepts: while, if-else, functions
Requirements
•	Generate a random number from 1 to 100.
•	Ask the player to guess the number.
•	Display “Too high” or “Too low.”
•	Limit the player to seven attempts.
•	Display the final result.
Bonus: Add easy, medium, and hard difficulty levels with different attempt limits.
''')
import random

def guess():
    number = random.randint(1,100)
    return number


while True:
    print("\n----------Number Guessing Game-------------")
    print("1.To play game")
    print("2.To end game")

    choice = int(input("enter choice :"))

    if choice == 1:
        print("Let's Start the game")
        print("You have 7 attempts only to guess the number")

        number = guess()
        count = 0

        while count < 7:
            user = int(input("enter your guess : "))
            count+=1

            if user == number:
                print("Congratulations! You have guessed the correct number",user)

            elif user > number:
                print("Too High!")
            
            else:
                print("Too Low!")

        if count == 7 and user!=number:
            print("You have lost the game")
            print("The correct number was ",number)

    elif choice == 2:
        print("Thank you for playing!")
        break

    else:
        print("Invalid Choice! Choose between 1 and 2")


    
