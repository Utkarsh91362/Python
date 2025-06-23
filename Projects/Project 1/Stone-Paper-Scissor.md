#project

Stone Paper Scissor game [[main.py]]


---

### ✅ Step 1: Importing Required Module

```python
import random
```

* You're importing Python’s built-in `random` module, which allows you to generate random choices — necessary for the computer to randomly pick Rock, Paper, or Scissors.

---

### ✅ Step 2: Defining the Win Conditions

```python
win_map = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}
```

* This dictionary defines **which move beats which**:

  * Rock beats Scissors
  * Paper beats Rock
  * Scissors beats Paper

So if `user = Rock` and `computer = Scissors`, then the user wins because `win_map["Rock"] == "Scissors"`.

---

### ✅ Step 3: Creating the List of Valid Choices

```python
choices = list(win_map.keys())
```

* This creates a list: `["Rock", "Paper", "Scissors"]`, which is used:

  * To randomly choose the computer's move
  * To validate the user's input

---

### ✅ Step 4: Computer's Random Choice

```python
def computers_choice():
    return random.choice(choices)

computer = computers_choice()
```

* `computers_choice()` randomly picks one of the three options.
* Then, `computer = computers_choice()` stores the random result in the variable `computer`.

---

### ✅ Step 5: User's Input and Validation

```python
def users_choice():
    i = input("Choose Rock/Paper/Sissors: ").capitalize()
    while(i not in choices):
        print("Enter a valid choice!")
        i = input("Choose Rock/Paper/Sissors: ").capitalize()
    return i

user = users_choice()
```

* `input()` takes the user’s move.
* `.capitalize()` fixes input like `"rock"` to `"Rock"` to match what's in `choices`.
* If input is invalid (not in `choices`), it loops until a valid choice is entered.
* The valid choice is then stored in `user`.

---

### ✅ Step 6: Determining the Winner

```python
def who_won():
    if(user == computer):
        return ("It's a Draw")
    else:
        if(win_map[user] == computer):
            return ("You won!")
        else:
            return ("You Loose!")
```

* If the user's and computer’s choices are the same → **Draw**
* If the user’s move **beats** the computer’s move according to `win_map`, the user wins.
* Otherwise, the user loses.

📝 Note: **"Loose"** is a typo — it should be `"You Lose!"`

---

### ✅ Step 7: Printing the Results

```python
print(f"The computer chose: {computer}")
print(f"The user chose: {user}")
print(who_won())
```

* Displays what both the computer and user chose.
* Shows the result of the game (Win, Lose, or Draw).

---

### ✅ Output Example:

```
['Rock', 'Paper', 'Scissors']
Choose Rock/Paper/Sissors: rock
The computer chose: Paper
The user chose: Rock
You Lose!
```

---

### ✅ Summary:

* You’ve built a working **Rock-Paper-Scissors** game.
* Computer randomly chooses a move.
* User inputs and validates their move.
* Game logic compares the two to decide the winner.
* Result is printed at the end.



