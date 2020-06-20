def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    heap_sort(input_list)
    num_1 = ""
    num_2 = ""
    i = len(input_list) - 1
    if i < 1:
        return None
    while i >= 0:
        if input_list[i] < 0:
            return None
        if i % 2 == 0:
            num_1 += str(input_list[i])
        else:
            num_2 += str(input_list[i])
        i -= 1
    return [int(num_1), int(num_2)]

# heapify subtree rooted at index root
def heapify(arr, n, root, ascending = True):
    new_root = root
    left = 2 * root + 1
    right = 2 * root + 2

    # check if root must be replaced
    if ascending:
        if left < n and arr[new_root] < arr[left]:
            new_root = left
        if right < n and arr[new_root] < arr[right]:
            new_root = right
    elif not ascending:
        if left < n and arr[new_root] > arr[left]:
            new_root = left
        if right < n and arr[new_root] > arr[right]:
            new_root = right
    
    # swap root if needed
    if new_root != root:
        arr[root], arr[new_root] = arr[new_root], arr[root]
        # recurse with the new root
        heapify(arr, n, new_root, ascending)

def heap_sort(arr, ascending = True):
    n = len(arr)

    # build a heap (maxheap if ascending, minheap if not ascending)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, ascending)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0, ascending)


def eval_test(test_number, input_str, expected_output_list, actual_output_list):
    print("")
    print("TEST CASE " + str(test_number))
    print("===========")
    print("- input: " + str(input_str))
    if expected_output_list:
        print("- expected output: " + str(expected_output_list) + " (sum = " + str(sum(expected_output_list)) + ")")
    else:
        print("- expected output: " + str(expected_output_list))
    if actual_output_list:
        print("- actual output: " + str(actual_output_list) + " (sum = " + str(sum(actual_output_list)) + ")")
    else:
        print("- actual output: " + str(actual_output_list))
    if expected_output_list and actual_output_list:
        if sum(expected_output_list) == sum(actual_output_list):
            print("Pass")
        else:
            print("Fail")
    else:
        if expected_output_list == actual_output_list:
            print("Pass")
        else:
            print("Fail")       
    print("")

# test case 1
n = [[1, 2, 3, 4, 5], [542, 31]]
result = rearrange_digits(n[0])
eval_test(1, n, n[1], result)

# test case 2
n = [[4, 6, 2, -5, 9, 8], None]
result = rearrange_digits(n[0])
eval_test(2, n, n[1], result)

# test case 3
n = [[], None]
result = rearrange_digits(n[0])
eval_test(3, n, n[1], result)

# test case 4
n = [[1], None]
result = rearrange_digits(n[0])
eval_test(4, n, n[1], result)

# test case 5
n = [[1, 2], [1, 2]]
result = rearrange_digits(n[0])
eval_test(5, n, n[1], result)

# test case 6
n = [[4, 6, 2, 5, 9, 8], [964, 852]]
result = rearrange_digits(n[0])
eval_test(6, n, n[1], result)

"""
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
"""