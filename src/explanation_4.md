# Problem 4: Dutch National Flag Problem
## Time complexity
In this case, we must not only adhere to the O(n) time constraint. We can only traverse the array once. But since we know that there are only 3 values (0, 1 and 2), we can push 0 values to the front, and 2 values to the back. This way it is quite straightforward to sort the array in a single traversal.
## Space complexity
The sorting is performed in place without using any other data structure, thus with O(1) space complexity.