# Problem 2: Search in a Rotated Sorted Array
## Time complexity
The trickiest part of this problem is finding the pivot index in the array, which we can do through binary search in O(logn). Once that we know where the pivot is, we can perform binary search on the array parts to find the index of the element that we are looking for.
## Space complexity
Both the pivot and element search are performed recursively, so we are using O(logn) space from the stack.