def merge_lists(list1, list2):
    """Merge two sorted lists into a single sorted list."""
    merged = []
    i, j = 0, 0

    # Traverse both lists and pick the smaller element
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from list1
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Append any remaining elements from list2
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

if __name__ == "__main__":
    # Example usage text output
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    print("Merged Result:", merge_lists(l1, l2))