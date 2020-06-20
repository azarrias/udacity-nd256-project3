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
    
    low, high = 1, number
    while low < high:
        avg = (low + high) // 2
        if avg ** 2 <= number and (avg + 1) ** 2 > number:
            return avg
        elif avg ** 2 > number:
            high = avg
        else:
            low = avg

def eval_test(test_number, input_str, expected_output_str, actual_output_str):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- input: " + str(input_str))
    print("- expected output: " + str(expected_output_str))
    print("- actual output: " + str(actual_output_str))
    if expected_output_str == actual_output_str:
        print("Pass")
    else:
        print("Fail")
    print("")

# test case 1
n = 0
result = sqrt(n)
eval_test(1, n, 0, result)

# test case 2
n = 2
result = sqrt(n)
eval_test(2, n, 1, result)

# test case 3
n = -5
result = sqrt(n)
eval_test(3, n, None, result)

# test case 4
n = None
result = sqrt(n)
eval_test(4, n, None, result)

# test case 5
n = 121
result = sqrt(n)
eval_test(5, n, 11, result)

"""
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
"""