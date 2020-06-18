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
    while i >= 0:
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
        if left < n and arr[root] < arr[left]:
            new_root = left
        if right < n and arr[new_root] < arr[right]:
            new_root = right
    elif not ascending:
        if left < n and arr[root] > arr[left]:
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

    # build a heap (minheap if ascending, maxheap if not ascending)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, ascending)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
