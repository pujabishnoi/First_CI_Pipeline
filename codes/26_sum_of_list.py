def sum_list(numbers):
    """Return the sum of all numbers in a list. Return 0 for an empty list."""
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        nums = [float(x) for x in user_input.split()]
        print("Sum of list elements:", sum_list(nums))
    except ValueError:
        print("Please enter valid numerical digits only.")