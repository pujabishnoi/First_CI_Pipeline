def rotate_list(elements, k):
    """Rotate a list to the right by k positions."""
    if not elements:
        return []

    # Handle cases where k is larger than the list length
    k = k % len(elements)

    # Slice and recombine the list
    return elements[-k:] + elements[:-k]

if __name__ == "__main__":
    user_input = input("Enter items separated by spaces: ").split()
    try:
        positions = int(input("Enter rotation positions (k): "))
        print("Rotated list:", rotate_list(user_input, positions))
    except ValueError:
        print("Please enter a valid integer for position.")