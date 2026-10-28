# 🃏 Blackjack Game

## 📌 Description
A command-line Blackjack game built with Python. The player competes against the computer by drawing cards and trying to achieve a score as close to 21 as possible without exceeding it.

## ✨ Features
- Random card dealing.
- Two initial cards for the player and computer.
- Option to draw another card or pass.
- Automatic handling of Aces (11 or 1) in certain situations.
- Computer draws cards while its score is below 17.
- Determines the winner based on final scores.
- Option to play multiple rounds.
- ASCII art logo displayed at the start of each round.

## 🛠️ Technologies Used
- Python 3
- `random` module
- Functions
- Lists and loops
- Conditional statements
- Type hints
- Custom module imports

## 📁 Project Structure

```text
Day-10-Blackjack-Game/
├── main.py
├── art.py
└── README.md
```

## 🚀 How to Run

1. Install Python 3.
2. Make sure `main.py` and `art.py` are in the same folder.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python main.py
```

## 🎮 How to Play

1. Enter `y` to start a game.
2. The player and computer each receive two cards.
3. View your cards and current score.
4. Enter `y` to draw another card or `n` to pass.
5. The computer draws cards until its score reaches at least 17 or it cannot draw without exceeding 21.
6. The final scores determine the winner.
7. Choose whether to play another round.

## 💻 Example Output

```text
Do you want to play a game of Blackjack? Type 'y' or 'n' : y

Your cards: [10, 7], current score: 17
computer's first card:  9
Type 'y' to get another card, Type 'n' to pass: n

Your cards: [10, 7], final score: 17
computer cards: [9, 8], final score: 17
Draw
```

*The cards and results will vary because they are randomly generated.*

## 📚 Learning Outcomes
- Generating random values using Python.
- Working with lists and functions.
- Calculating scores using `sum()`.
- Implementing game logic with loops and conditional statements.
- Handling special cases for Aces.
- Comparing scores to determine the winner.

## 👨‍💻 Author
**Dipendra Kushwaha**

GitHub: [@Dipu252](https://github.com/Dipu252)
