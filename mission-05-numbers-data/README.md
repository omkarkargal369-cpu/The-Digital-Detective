# Mission 5 — Numbers and data

## 1. Task / objective
Do manual number conversions between decimal, binary, and hex, verify them in Python, write a `number_converter.py` script, and answer questions about text encoding like ASCII and UTF-8.

## 2. Work completed
- Did all 7 number conversions by hand showing step-by-step working.
- Verified all 7 answers in Python terminal.
- Built and tested `number_converter.py` with 3 test numbers (42, 100, 255).
- Looked up ASCII codes for A and a, and explained why computers need text encoding.
- Used zero tables anywhere in this file.

## 3. Commands / tools used
- Python interactive shell (`python3`) to test built-in functions: `bin()`, `hex()`, and `int()`.
- `python3 mission-05-numbers-data/number_converter.py` - ran the converter script.
- Python built-in `ord()` to verify character decimal codes.

## 4. My understanding

### Task 5.1 — Manual Conversions (Working and Answers)

1. Decimal 13 to binary:
   - 13 / 2 = 6, remainder 1
   - 6 / 2 = 3, remainder 0
   - 3 / 2 = 1, remainder 1
   - 1 / 2 = 0, remainder 1
   - Reading remainders from bottom to top: `1101`

2. Decimal 25 to binary:
   - 25 / 2 = 12, remainder 1
   - 12 / 2 = 6, remainder 0
   - 6 / 2 = 3, remainder 0
   - 3 / 2 = 1, remainder 1
   - 1 / 2 = 0, remainder 1
   - Reading remainders from bottom to top: `11001`

3. Binary 1010 to decimal:
   - (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0)
   - 8 + 0 + 2 + 0 = `10`

4. Binary 1101 to decimal:
   - (1 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0)
   - 8 + 4 + 0 + 1 = `13`

5. Hexadecimal A to decimal:
   - In hex, digits go 0-9 then A=10, B=11, C=12, D=13, E=14, F=15.
   - So A = `10`

6. Hexadecimal 1F to decimal:
   - (1 * 16^1) + (15 * 16^0)
   - 16 + 15 = `31`

7. Binary 1111 to hexadecimal:
   - 1111 in decimal = 8 + 4 + 2 + 1 = 15.
   - 15 in hex is represented by the letter `F`.

---

### Task 5.2 — Python Verification
Tested each in Python interactive mode:
- `bin(13)` returned `'0b1101'` -> Matches manual answer 1101.
- `bin(25)` returned `'0b11001'` -> Matches manual answer 11001.
- `int('1010', 2)` returned `10` -> Matches manual answer 10.
- `int('1101', 2)` returned `13` -> Matches manual answer 13.
- `int('A', 16)` returned `10` -> Matches manual answer 10.
- `int('1F', 16)` returned `31` -> Matches manual answer 31.
- `hex(0b1111)` returned `'0xf'` -> Matches manual answer F.

---

### Task 5.3 — Number Converter Script
Created `number_converter.py` using `input()`, `int()`, `bin()`, and `hex()`.

Test runs:
- Test 1: Entered `42`
  - Binary output: `101010` (or `0b101010`)
  - Hexadecimal output: `2A` (or `0x2A`)
- Test 2: Entered `100`
  - Binary output: `1100100` (or `0b1100100`)
  - Hexadecimal output: `64` (or `0x64`)
- Test 3: Entered `255`
  - Binary output: `11111111` (or `0b11111111`)
  - Hexadecimal output: `FF` (or `0xFF`)

What the functions do:
- `bin(number)`: Converts an integer into a binary string starting with `0b`.
- `hex(number)`: Converts an integer into a base-16 hexadecimal string starting with `0x`.

---

### Task 5.4 — Text Encoding
- ASCII decimal code for uppercase A: `65` (tested with `ord('A')`).
- ASCII decimal code for lowercase a: `97` (tested with `ord('a')`).
- Why computers need an encoding standard:
  Computers only store electrical charges and 1s and 0s. They have no idea what the letter "A" or a comma is unless there is an agreed lookup table telling them which binary number represents which symbol. Without that, text saved on one machine would just show up as random garbage on another.
- One character not in basic ASCII:
  The Indian Rupee symbol `₹` (or emoji like `🔥`). Basic ASCII only supports 128 English characters (numbers 0-127), so other languages and symbols require UTF-8.

## 5. Difficulties faced
Remembering that Python's `bin()` and `hex()` prefix the output with `0b` and `0x`, so I used string slicing `[2:]` in the script to get clean values.

## 6. How I resolved them
Used `[2:]` in `number_converter.py` so it prints the clean digits alongside the prefixed version.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- `mission-05-numbers-data/README.md`

## 8. Commit details
- Commit message: "Build number converter and practise data representation"
- Ready to push to GitHub.
