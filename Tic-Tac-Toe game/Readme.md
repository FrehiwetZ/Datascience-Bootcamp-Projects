# ❌⭕ Tic-Tac-Toe (CLI Game in Python)

## 📌 Overview

This project is a command-line (CLI) implementation of the classic Tic-Tac-Toe game. It allows two players to play against each other by taking turns and entering their moves through the keyboard.

---

## 🚀 Features

* Two-player mode (Player X and Player O)
* Interactive command-line interface
* Input validation (prevents invalid moves)
* Win detection (rows, columns, diagonals)
* Draw detection
* Clean and simple design

---

## 🧠 How It Works

1. The game initializes a 3×3 board
2. Players take turns entering their move (row and column)
3. The program validates the input
4. The board is updated after each move
5. The game checks:

   * If a player has won
   * If the game is a draw
6. The game continues until there is a winner or a draw

---

## 🧾 Code Structure

### Main Functions:

* `print_board(board)` → Displays the game board
* `check_winner(board, player)` → Checks if a player has won
* `is_draw(board)` → Checks if the board is full
* `tic_tac_toe()` → Controls the main game flow

---

## ▶️ How to Run

1. Save the file as `tic_tac_toe.py`
2. Open terminal or command prompt
3. Navigate to the file location
4. Run:

```bash
python tic_tac_toe.py
```

---

## 🎮 How to Play

* The board positions are numbered from **1 to 3**
* Players enter their move as:

```text
row column
```

### Example:

```text
1 2
```

👉 This places the mark in **Row 1, Column 2**

---

## 📥 Example Gameplay

```text
  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Player X, enter row and column: 1 1

X |   |  
--+---+--
  |   |  
--+---+--
  |   |  
```

---

## ⚠️ Notes

* Only numbers between 1 and 3 are allowed
* Players cannot overwrite an occupied cell
* The game runs until a win or draw occurs

---

## 📚 Concepts Used

* Functions
* Loops (`while`, `for`)
* Conditional statements (`if`)
* Lists (2D list for board)
* Input handling
* Error handling (`try-except`)

---

## 💡 Future Improvements

* Add replay option
* Add score tracking
* Implement AI opponent
* Create a graphical user interface (GUI)

---

## 👨‍💻 Author
Name: Frehiwet Zerihun
Date: April 6,2026G.c
