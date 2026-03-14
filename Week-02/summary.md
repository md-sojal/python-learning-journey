# Week 02 Progress (07 March – 14 March 2026)

This week I continued my Python learning journey through Harvard's CS50P while balancing full-time work and university assignments.

It was a tough week personally, but I pushed through and coded every single day — even on the day I said I'd take off.

---

# 📚 Topics Covered

## Loops (Continued)
- List comprehensions
- Dictionary comprehensions
- Comprehension filtering with conditions

## Tuples
- Tuple unpacking
- Using tuples for coordinate data

## String Slicing
- Slicing syntax and index ranges

## Exception Handling
- `try` and `except` blocks
- `ValueError` handling
- How to `raise` errors
- Types of errors in Python
- Debugging with breakpoints

## Libraries and Modules
- `import` and `from` syntax
- The `random` module — `choice()` and `randint()`
- The `statistics` module
- The `sys` module — `sys.argv`, `sys.exit()`
- List slicing with `sys.argv`
- The `requests` library for API calls
- `response.raise_for_status()`
- Parsing JSON responses with `.json()`
- `pip` and `cowsay`
- How to package a program as a module
- `__name__` and `__init__.py`
- Creating and importing custom packages

## GUI with tkinter
- `tk.Tk()` — the root window
- `tk.Label()` — displaying text
- `tk.Button()` — clickable buttons
- `tk.Text()` — multi-line text input
- `tk.Menu()` — menu bars
- `.pack()` and `.grid()` — layout managers
- `.config()` — updating widget properties
- `.after()` — scheduling repeated function calls
- `messagebox` — pop-up dialogs
- `filedialog` — file open and save dialogs
- `root.mainloop()` — running the GUI loop

## File Handling (via CS50 examples)
- Reading files with `open()`
- Writing CSV files with `csv.writer`
- Using `re` (regular expressions) for text cleanup

---

# 💻 Programs I Built

### 1. Word Frequency Counter
A program that reads a text file, counts how many times each word appears using list and dictionary comprehensions, and saves the result to a CSV file.

Files: `comprehensions/comprehensions.py`, `comprehensions/helpers.py`

Concepts used:
- List comprehensions with filtering
- Dictionary comprehensions
- File I/O
- `csv` module
- `re` module for text cleaning

---

### 2. Sokoban Action History
Simulates a game action log with undo and restart functionality using list methods.

File: `sokuban.py`

Concepts used:
- Lists
- `.pop()` and `.clear()`
- `while` loops

---

### 3. Location Coordinates
Unpacks a tuple of GPS coordinates and prints latitude and longitude separately.

File: `locations.py`

Concepts used:
- Tuples
- Tuple unpacking
- f-strings

---

### 4. Soil Moisture Simulator
Simulates soil moisture levels dropping over days. Uses a global variable in a helper module that gets updated each time it is sampled.

Files: `soil_moisture/soil.py`, `soil_moisture/water.py`

Concepts used:
- `global` keyword
- `random.randint()`
- Module imports
- `while` loops

---

### 5. Coin Toss Game
A coin flip guessing game. Thought of independently while learning about `random.choice()` and `randint()`.

File: `coin_toss.py`

Concepts used:
- `random.choice()`
- Conditionals
- `.lower()` for input normalization

---

### 6. Number Guessing Game
A guessing game where the user picks how many tries they get, with a live countdown each round.

File: `guess.py`

Concepts used:
- `random.randint()`
- `for` loop with `range()`
- `break` and `else` on loops

---

### 7. Rent and Expense Splitter
Calculates each person's share of rent, food, and electricity costs. Built independently in own style after watching videos for inspiration — not copied.

File: `rent_calculator.py`

Concepts used:
- `try` / `except ValueError`
- Arithmetic
- f-strings

---

### 8. Rock Paper Scissors
A fully playable Rock Paper Scissors game against the computer. Built independently in own style.

File: `rock_paper_scissor.py`

Concepts used:
- `from random import choice`
- `.capitalize()` for input normalization
- `elif` chain for game logic
- Input validation

---

### 9. Tic-Tac-Toe GUI
A two-player Tic-Tac-Toe game with a graphical interface. Watched a video to understand the logic and flow but focused on understanding each part rather than copying.

File: `tic_tac_toe.py`

Concepts used:
- `tkinter` buttons and grid layout
- `global` variables
- Win condition checking with index combinations
- `messagebox`

---

### 10. Digital Clock GUI
A live digital clock that updates every second on screen.

File: `clock.py`

Concepts used:
- `tkinter` Label and `.after()`
- `strftime` for time formatting
- `root.mainloop()`

---

### 11. Text Editor GUI
A functional text editor with New, Open, Save, and Exit menu options. Built on a rest day — couldn't stop coding.

File: `notepad.py`

Concepts used:
- `tkinter` Menu and Text widget
- `filedialog.askopenfilename()` and `asksaveasfilename()`
- `messagebox`
- File read and write

---

### 12. Task Manager
A command-line task manager with options to add, update, delete, and view tasks.

File: `to_do.py`

Concepts used:
- Lists
- `list.index()`
- `del`
- `while` loop with a menu system

---

### 13. Art Institute of Chicago Search
Searches the Art Institute of Chicago API by artist or artwork name. Started as a single-file program and was then refactored into a proper package structure with separate modules.

Files: `search/search.py`, `search/museum/artists.py`, `search/museum/artwork.py`

Concepts used:
- `requests` library
- API calls and JSON parsing
- `response.raise_for_status()`
- Custom package with `__init__.py`
- Importing from a custom package

---

# 🧠 Key Lessons Learned

This week helped me understand:

- How comprehensions make loops shorter and more readable
- How `try`/`except` prevents programs from crashing on bad input
- How the `random` module opens up game and simulation logic
- How `tkinter` works — `root` is the window, widgets sit inside it, and `.mainloop()` keeps everything running
- How to structure a project as a proper package using `__init__.py`
- How to make real API calls and parse JSON responses
- That `global` allows a variable to be shared and updated across function calls within a module

I still want to deepen my understanding of `helpers.py` — specifically how `re` cleans text and how `csv.writer` works. The `tkinter` Label and `.after()` scheduling also needs more practice.

---

# 🚀 Next Week Goals

For Week 3 I plan to:

- Continue with CS50P
- Keep building at least one small program per day
- Revisit `helpers.py` to fully understand `re` and `csv.writer`
