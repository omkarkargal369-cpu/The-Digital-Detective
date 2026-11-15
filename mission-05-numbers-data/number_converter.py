def main():
    user_input = input("Enter a positive whole number: ")
    try:
        num = int(user_input)
        if num < 0:
            print("Please enter a positive number!")
            return
        
        # bin() adds '0b' prefix, hex() adds '0x' prefix
        binary_val = bin(num)[2:]
        hex_val = hex(num)[2:].upper()
        
        print(f"Decimal: {num}")
        print(f"Binary: {binary_val} (or 0b{binary_val})")
        print(f"Hexadecimal: {hex_val} (or 0x{hex_val})")
    except ValueError:
        print("That is not a valid integer.")

if __name__ == "__main__":
    main()
