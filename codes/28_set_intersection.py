def set_intersection(first, second):
    """Return a list containing elements present in both input lists, without duplicates."""
    intersection = []
    for item in first:
        if item in second and item not in intersection:
            intersection.append(item)
    return intersection

if __name__ == "__main__":
    list1 = input("Enter first list items separated by spaces: ").split()
    list2 = input("Enter second list items separated by spaces: ").split()
    print("Intersection:", set_intersection(list1, list2))