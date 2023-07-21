def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral

def main():
    try:
        num = int(input("Enter an integer (1 to 3999): "))
        if 1 <= num <= 3999:
            roman_numeral = int_to_roman(num)
            print(f"The Roman numeral representation of {num} is: {roman_numeral}")
        else:
            print("Please enter a valid integer between 1 and 3999.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()