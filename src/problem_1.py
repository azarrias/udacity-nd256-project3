def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return None
    elif number in [0, 1]:
        return number
    
    low, high = 2, number
    while low < high:
        avg = (low + high) // 2
        if avg ** 2 <= number and (avg + 1) ** 2 > number:
            return avg
        elif avg ** 2 > number:
            high = avg
        else:
            low = avg
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")