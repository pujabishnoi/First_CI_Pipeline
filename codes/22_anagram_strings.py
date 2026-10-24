def is_anagram(first, second):
    """Return True if first and second strings are anagrams."""
    # Remove spaces and convert to lowercase for accurate matching
    clean_first = first.replace(" ", "").lower()
    clean_second = second.replace(" ", "").lower()
    return sorted(clean_first) == sorted(clean_second)

if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    if is_anagram(str1, str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")