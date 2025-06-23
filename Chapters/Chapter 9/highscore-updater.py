import random  # Import the random module to generate random numbers

# Define a function to simulate the game
def game():
    print("The Game begins...")

    # Generate a random score between 25 and 90
    score = random.randint(25, 90)
    print(f"You scored.... {score} points ")

    # Open the highscore file to read the current high score
    with open("txt files/highscore.md") as f:
        highscore = f.read()  # Read contents of the file

        # Check if file was not empty, and convert it to an integer
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0  # If the file is empty, assume highscore is 0

    # Compare current score to the high score
    if score > highscore:
        # If the new score is higher, update the file with the new high score
        with open("txt files/highscore.md", "w") as f:
            f.write(str(score))  # Write new score as a string
            print("Congrats you created a new highscore!")
    else:
        # If not higher, print the previous high score
        print(f"Previous Highscore was... {highscore}")

    return score  # Return the current score (optional)

# Start the game by calling the function
game()
