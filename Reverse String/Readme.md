# 🔁 Reverse String in Python

## 📌 Overview

This is a simple Python program that reverses a given input. The program is designed to be beginner-friendly and demonstrates basic Python concepts such as functions, string manipulation, and input handling.

---

## 🚀 Features

* Reverses any input (string, number, etc.)
* Automatically converts input to a string
* Uses simple and efficient Python syntax
* Easy to understand and modify

---

## 🧠 How It Works

1. The input is passed to a function.
2. The function converts the input into a string using `str()`.
3. The string is reversed using slicing (`[::-1]`).
4. The reversed result is returned or printed.

---

## 🧾 Code Example

```python
def reverse_string(text):
    # Convert input to string
    text = str(text)
    
    # Reverse the string
    return text[::-1]


# Example usage
print(reverse_string("hello"))   # Output: olleh
print(reverse_string(12345))     # Output: 54321
```

---

## ▶️ How to Run

1. Save the file as `reverse.py`
2. Open a terminal or command prompt
3. Navigate to the file location
4. Run the command:

```bash
python reverse.py
```

---

## 📥 Example Input & Output

| Input      | Output     |
| ---------- | ---------- |
| `"hello"`  | `"olleh"`  |
| `12345`    | `"54321"`  |
| `"Python"` | `"nohtyP"` |

---

## ⚠️ Notes

* All inputs are converted to strings before reversing
* Output is always a string
* Works with numbers, lists, and other data types (converted to string)

---

## 📚 Concepts Used

* Functions
* String slicing
* Type conversion (`str()`)
* Basic input/output

---

## 💡 Future Improvements

* Add user input from the keyboard
* Add input validation
* Build a GUI or web version

---

## 👨‍💻 Author
Name: Frehiwet Zerihun
Date:April 6 ,2026G.C

Simple Python practice project for learning and understanding basic programming concepts.
