def is_armstrong_number(num):
    # Calculate the number of digits in 'num'
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of 'num_digits'
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the number is an Armstrong number
    return num == digit_sum

def generate_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Example usage:
start_range = 1
end_range = 1000
armstrong_list = generate_armstrong_numbers(start_range, end_range)
print(armstrong_list)
