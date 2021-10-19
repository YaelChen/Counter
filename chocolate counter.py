def chocolate_counter(eight_digit_no):
    """
    the function gets a number in which 0 represent a whole cube and 1 a broken one, and counts the broken cubes.
    :param eight_digit_no: an 8 digit number from 0 and 1 only.
    :type eight_digit_no: str
    :return: the number of broken cubes
    :rtype: int
    """
    counter = 0
    for num in eight_digit_no:
        if num == "1":
            counter += 1
    return counter


print(chocolate_counter("01011001"))
