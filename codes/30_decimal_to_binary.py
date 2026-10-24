def decimal_to_binary(n):
    """Convert a non-negative decimal integer to its binary string representation."""
    if n < 0:
        raise ValueError("Only non-negative integers are supported.")
    if n == 0:
        return "0"
        
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2
    return binary_str

if __name__ == "__main__":
    try:
        val = int(input("Enter a non-negative decimal number: "))
        print("Binary representation:", decimal_to_binary(val))
    except ValueError as e:
        print(e)