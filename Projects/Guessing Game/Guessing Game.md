#project

Guessing Game main file [[Python/Projects/Guessing Game/main.py]]


---

## 🎮 Number Guessing Game — Python Code Explanation

This Python program is a simple **number guessing game** where the user tries to guess a number randomly selected by the computer between 1 and 30.

---

### 🔁 Program Flow

1. The **computer** picks a random number between 1 and 30 using the `random.randint()` function.
    
2. The user is prompted to enter a guess.
    
3. After each guess, the program gives a hint:
    
    - **"Try higher"** if the guess is too low.
        
    - **"Try lower"** if the guess is too high.
        
    - **"Perfect you guessed it right!"** if the guess is correct.
        
4. The program counts the number of attempts.
    
5. The user can type `Q` to quit the game anytime.
    

---

### 🧠 Code Breakdown

```python
import random
```

- Imports the `random` module to generate random numbers.
    

```python
count = 0
```

- A global variable to keep track of how many guesses the user made.
    

```python
def computer_chose():
    c = random.randint(1, 30)
    return int(c)
```

- Generates a random number between 1 and 30 and returns it.
    

```python
def users_choice():
    n = input("Choose a number: ")
    if n.upper() == "Q":
        return "Q"
    else:
        return int(n)
```

- Asks the user to enter a number.
    
- If the user types `Q` or `q`, the function returns `"Q"` to quit the game.
    
- Otherwise, the input is converted to an integer and returned.
    

```python
def guessing(user, computer):
    global count
    count += 1
    if computer == user:
        print("Perfect you guessed it right!")
        return True
    elif computer > user:
        print("Try higher!")
    elif computer < user:
        print("Try lower!")
    return False
```

- Compares the user's guess with the computer's number.
    
- Increments the guess count.
    
- Returns `True` if guessed correctly, else `False`.
    

```python
def play_game(computer):
    print("Welcome to the Guessing game!")
    while True:
        user = users_choice()
        if user == "Q":
            print("You quit the game")
            break
        elif user is None or not 1 <= user <= 30:
            print("Pick a number between 1-30")
            continue
        if guessing(user, computer):
            break
    print(f"NO. of guesses you took: {count}")
    return computer
```

- Runs the actual game loop.
    
- Keeps accepting guesses until the correct one is entered or the user quits.
    
- At the end, displays the number of guesses made.
    

```python
comp = computer_chose()
play_game(comp)
```

- Picks the number once before the game starts.
    
- Calls `play_game()` to begin.
    

---

### 📝 Example Output

```
Welcome to the Guessing game!
Choose a number: 10
Try higher!
Choose a number: 20
Try lower!
Choose a number: 15
Perfect you guessed it right!
NO. of guesses you took: 3
```

---

### ✅ Features

- Validates user input.
    
- Handles quitting gracefully with `'Q'`.
    
- Efficient and simple logic with minimal memory usage.
    
- Modular structure using functions.
    

---

[[Python/Projects/Guessing Game/highscore|highscore]]
