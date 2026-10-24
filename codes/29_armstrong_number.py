def is_armstrong(number):
    """Return True if the number is an Armstrong number, otherwise False."""
    if number < 0:
        return False
        
    str_num = str(number)
    num_digits = len(str_num)
    
    total = sum(int(digit) ** num_digits for digit in str_num)
    return total == number

if __name__ == "__main__":
    try:
        val = int(input("Enter an integer: "))
        if is_armstrong(val):
            print(f"{val} is an Armstrong number.")
        else:
            print(f"{val} is not an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")