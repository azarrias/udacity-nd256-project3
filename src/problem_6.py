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

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")