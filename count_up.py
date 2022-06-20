def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_range
    # YOUR CODE HERE
    x = range(start, stop+1, 1)
    for num in x:
        print(num)

count_up(5, 7)
