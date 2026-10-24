def find_max_min(numbers):
    """Return a tuple (max, min) from a list without using max() or min()."""
    if not numbers:
        return None, None

    current_max = numbers[0]
    current_min = numbers[0]

    for num in numbers:
        if num > current_max:
            current_max = num
        if num < current_min:
            current_min = num

    return current_max, current_min

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        nums = [int(x) for x in user_input.split()]
        high, low = find_max_min(nums)
        print(f"Maximum: {high}, Minimum: {low}")
    except ValueError:
        print("Please enter valid numbers only.")