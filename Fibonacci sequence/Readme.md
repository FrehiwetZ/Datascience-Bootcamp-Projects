# 🔢 Fibonacci Sequence Generator (Python)

## 📌 Overview

This project is a simple Python program that generates a Fibonacci sequence up to a specified number of terms. It is designed for beginners to understand loops, variables, and basic algorithm logic.

---

## 🚀 Features

* Generates Fibonacci sequence up to *n* terms
* Accepts user input
* Uses simple and efficient logic
* Beginner-friendly and easy to understand

---

## 🧠 How It Works

1. The program takes a number `n` as input
2. It starts with the first two numbers: `0` and `1`
3. Each next number is calculated as the sum of the previous two
4. The sequence continues until `n` terms are generated

---

## 🧾 Code Example

```python
def fibonacci(n):
    # Convert input to integer
    n = int(n)
    
    a, b = 0, 1
    sequence = []

    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


# Example usage
num = input("Enter number of terms: ")
print(fibonacci(num))
```

---

## ▶️ How to Run

1. Save the file as `fibonacci.py`
2. Open terminal or command prompt
3. Navigate to the file location
4. Run:

```bash
python fibonacci.py
```

---

## 📥 Example Input & Output

| Input | Output                |
| ----- | --------------------- |
| 5     | [0, 1, 1, 2, 3]       |
| 7     | [0, 1, 1, 2, 3, 5, 8] |

---

## ⚠️ Notes

* Input is converted to an integer using `int()`
* Output is returned as a list
* Negative inputs are not handled in this version

---

## 📚 Concepts Used

* Functions
* Loops (`for`)
* Variables and assignment
* Lists
* Type conversion (`int()`)

---

## 💡 Future Improvements

* Add input validation (handle negative numbers)
* Print sequence instead of returning a list
* Add graphical visualization
* Implement recursive version

---

## 👨‍💻 Author

Name: Frehiwet Zerihun
Date: April 6,2026G.C
