def int_to_roman(number: int) -> str:
    """
    Takes an integer number, returns a string with the roman numeral.
        Parameters:
            number (int): A positive integer less than 5000
        Returns:
            numeral (str): The roman numeral of the number.
    """
    # Exception handling
    if(number <= 0): raise ValueError("Number is less than 1")
    if(number >= 5000): raise ValueError("Number is greater than 4999")
    
    # Start of algorithm
    # The algorithm starts with a long string of I's
    # and replaces rows of smaller letters with one greater letter
    # until the numeral is optimized
    letters = "IVXLCDM"

    # Create a long string of I's
    numeral = letters[0]*number

    for index, letter in enumerate(letters[:-1]):
        # Letters which are related to 5 (V, L, and D)
        if index % 2:
            # Row of VV is replaced with X
            numeral = numeral.replace(letter*2, letters[index + 1])
            # Row of VIV is replaced with IX
            numeral = numeral.replace(
                letter+letters[index - 1]+letter, letters[index - 1] + letters[index + 1])
        # Letters which are related to 10 (I, X, C and M)
        else:
            # Row of IIIII is replaced with V
            numeral = numeral.replace(letter*5, letters[index + 1])
            # Row of IIII is replaced with IV
            numeral = numeral.replace(letter*4, letter + letters[index + 1])
    
    return numeral

print(int_to_roman(4999))
