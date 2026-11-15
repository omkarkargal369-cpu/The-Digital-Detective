# Mission 4 — How programs run

## 1. Task / objective
Write and run a simple one-line Python script (`hello.py`) and compare how a compiler works versus an interpreter.

## 2. Work completed
- Made `hello.py` with `print("Hello from Python")`.
- Ran it using `python3` in terminal and verified the output.
- Compared compilers and interpreters using bullet points instead of tables.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py` - ran the script using Python 3 interpreter.
- Text editor to create the python file and this README.

## 4. My understanding

### Task 4.1 — Python Program Execution
Ran `python3 mission-04-programs/hello.py` and the terminal printed:
`Hello from Python`
Python loaded the script, parsed the print statement, and executed it right on the spot.

### Task 4.2 — Compiler vs Interpreter Comparison

**Compiler:**
- When translation / execution happens: Translates the whole source code file all at once into machine code before you can run it.
- Typical output: An executable binary file (like an `.exe` on Windows or a standalone binary on Mac/Linux).
- One example: C, C++, or Rust (using `gcc`, `clang`, or `rustc`).
- One advantage: Runs way faster once compiled because the machine code runs directly on the CPU without translation overhead.

**Interpreter:**
- When translation / execution happens: Reads and executes code line-by-line at runtime as the program runs.
- Typical output: Runs directly in memory, no separate standalone executable file created.
- One example: Python or JavaScript (Node.js).
- One advantage: Much easier and faster for testing and debugging because you don't have to wait for a build step every time you change a line of code.

**In my own words:**
A compiler is like taking an entire book in English and translating the whole thing into Hindi before anyone reads it, so reading it later is super fast. An interpreter is like a live translator standing next to you translating sentence by sentence as you speak, which is a bit slower but makes it super easy to change your words on the fly without waiting.

## 5. Difficulties faced
No issues here, the one-liner python script worked on the first try.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-04-programs/hello.py`
- `mission-04-programs/README.md`
- Terminal output: `Hello from Python`

## 8. Commit details
- Commit message: "Compare compilers and interpreters"
- Ready to push to GitHub.
