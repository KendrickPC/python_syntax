def print_upper_words(words_list, must_start_with):
    """This should print transform every letter, in list, into upper case and print"""
    for word in words_list:
        for target in must_start_with:
            if word.startswith(target):
                print(word.upper())
  

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})



# Transform word to upper case:
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/#:~:text=Output%3A%20geeksforgeeks%20geeksforgeeks-,upper(),all%20lowercase%20characters%20to%20uppercase.

# Starts With:
# https://www.tutorialspoint.com/python/string_startswith.htm