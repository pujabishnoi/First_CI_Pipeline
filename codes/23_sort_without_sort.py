def sort_list(numbers):
    """Sort a list of numbers in ascending order without using built-in sort methods."""
    n = len(numbers)
    # Make a copy so we don't modify the original input array directly
    arr = list(numbers)
    
    # Loop through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        nums = [int(x) for x in user_input.split()]
        print("Sorted list:", sort_list(nums))
    except ValueError:
        print("Please enter valid numbers only.")