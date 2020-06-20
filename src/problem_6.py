def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return None

    max_num = -float('Inf')
    min_num = float('Inf')

    for num in ints:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return (min_num, max_num)


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
n = [[4, 5, -2], (-2, 5)]
result = get_min_max(n[0])
eval_test(1, n[0], n[1], result)

# test case 2
n = [[], None]
result = get_min_max(n[0])
eval_test(2, n[0], n[1], result)

# test case 3
n = [[4], (4, 4)]
result = get_min_max(n[0])
eval_test(3, n[0], n[1], result)

# test case 4
n = [None, None]
result = get_min_max(n[0])
eval_test(4, n[0], n[1], result)

"""
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
"""