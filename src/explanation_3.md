# Problem 3: Rearrange Array Digits
## Time complexity
If we first sort the elements of the array, we can then assign the biggest value elements to the most significant digits of the output values. This way we can maximize the output values. I chose to do the sorting using a heapsort, since it will always respect the O(nlogn) constraint of the problem, for the best, average and worst case. 
## Space complexity
The other reason why I chose the heapsort algorithm is its O(1) space complexity, since the sorting is performed in place.