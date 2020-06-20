def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return None

    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1
    
    front_pos = 0
    
    while front_pos <= next_pos_2:
        if input_list[front_pos] == 0:
            input_list[front_pos] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_pos += 1
        elif input_list[front_pos] == 2:
            input_list[front_pos] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_pos += 1
    
    return input_list


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
n = [[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]]
input_copy = str(n[0])
result = sort_012(n[0])
eval_test(1, input_copy, n[1], result)

# test case 2
n = [[], []]
input_copy = str(n[0])
result = sort_012(n[0])
eval_test(2, input_copy, n[1], result)

# test case 3
n = [None, None]
input_copy = str(n[0])
result = sort_012(n[0])
eval_test(3, input_copy, n[1], result)

# test case 4
n = [[2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
input_copy = str(n[0])
result = sort_012(n[0])
eval_test(4, input_copy, n[1], result)

# test case 5
n = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]]
input_copy = str(n[0])
result = sort_012(n[0])
eval_test(5, input_copy, n[1], result)

"""
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
"""