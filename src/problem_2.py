def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot_index(input_list)
    if pivot == -1:
        return -1
    if input_list[pivot] == number:
        return pivot
    if input_list[0] <= number:
        return binary_search(input_list, number, 0, pivot - 1)
    return binary_search(input_list, number, pivot + 1, len(input_list) - 1)

def binary_search(input_list, number, low, high):
    if high < low:
        return -1
    mid = (low + high) // 2

    if input_list[mid] == number:
        return mid
    if input_list[mid] < number:
        return binary_search(input_list, number, mid + 1, high)
    return binary_search(input_list, number, low, mid - 1)

def find_pivot_index(input_list):
    return find_pivot_index_recursive(input_list, 0, len(input_list) - 1)

def find_pivot_index_recursive(input_list, low, high):
    # base case
    if high < low:
        return -1
    elif high == low:
        return low

    mid = (low + high) // 2
    if mid < high and input_list[mid] > input_list[mid + 1]:
        return mid
    if mid > low and input_list[mid] < input_list[mid - 1]:
        return mid - 1
    if input_list[low] >= input_list[mid]:
        return find_pivot_index_recursive(input_list, low, mid - 1)
    return find_pivot_index_recursive(input_list, mid + 1, high)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
