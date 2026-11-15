# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers by hand, check them in Python, write a simple `number_converter.py` program, and learn about ASCII.

## 2. Work completed
- Did all 7 number conversions showing simple math steps.
- Checked each one using Python's `bin()`, `hex()`, and `int()`.
- Wrote a simple `number_converter.py` script and tested it with 3 numbers.
- Looked up ASCII codes for A and a.

## 3. Commands / tools used
- `python3` - used to test `bin()`, `hex()`, and `int()`.
- `python3 number_converter.py` - ran the script.
- `ord()` - checked character ASCII numbers.

## 4. My understanding

### Task 5.1 — Manual Conversions
1. Decimal 13 to binary:
   - 13 / 2 = 6 r 1
   - 6 / 2 = 3 r 0
   - 3 / 2 = 1 r 1
   - 1 / 2 = 0 r 1
   - Answer: `1101`

2. Decimal 25 to binary:
   - 25 / 2 = 12 r 1
   - 12 / 2 = 6 r 0
   - 6 / 2 = 3 r 0
   - 3 / 2 = 1 r 1
   - 1 / 2 = 0 r 1
   - Answer: `11001`

3. Binary 1010 to decimal:
   - 1*8 + 0*4 + 1*2 + 0*1 = 8 + 2 = `10`

4. Binary 1101 to decimal:
   - 1*8 + 1*4 + 0*2 + 1*1 = 8 + 4 + 1 = `13`

5. Hexadecimal A to decimal:
   - In hex, A is `10`

6. Hexadecimal 1F to decimal:
   - 1*16 + 15*1 = 16 + 15 = `31`

7. Binary 1111 to hexadecimal:
   - 1111 in decimal is 15. In hex, 15 is `F`.

### Task 5.2 — Python Checks
- `bin(13)` gave `'0b1101'` (matches 1101)
- `bin(25)` gave `'0b11001'` (matches 11001)
- `int('1010', 2)` gave `10` (matches 10)
- `int('1101', 2)` gave `13` (matches 13)
- `int('A', 16)` gave `10` (matches 10)
- `int('1F', 16)` gave `31` (matches 31)
- `hex(0b1111)` gave `'0xf'` (matches F)

### Task 5.3 — Number Converter Program
Code inside `number_converter.py`:
```python
num = int(input("Enter a number: "))

b = bin(num)
h = hex(num)

print("Binary:", b)
print("Hexadecimal:", h)
```

Tests:
- Input `42` -> Binary: `0b101010`, Hexadecimal: `0x2a`
- Input `100` -> Binary: `0b1100100`, Hexadecimal: `0x64`
- Input `255` -> Binary: `0b11111111`, Hexadecimal: `0xff`

What the functions do:
- `bin()`: Converts a number to binary (starts with `0b`).
- `hex()`: Converts a number to hexadecimal (starts with `0x`).

### Task 5.4 — Text Encoding
- ASCII code for uppercase A: `65`
- ASCII code for lowercase a: `97`
- Why computers need encoding: Computers only understand numbers, so they need a standard table to know which number stands for which letter.
- Character not in basic ASCII: The Indian rupee symbol `₹` or an emoji like `👍`.

## 5. Difficulties faced
No difficulties. Kept the python code very simple.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- `mission-05-numbers-data/README.md`

## 8. Commit details
- Commit message: "Build number converter and practise data representation"
- Pushed to main.
