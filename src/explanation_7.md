# Problem 7: Request Routing in a Web Server with a Trie
## Time complexity
This problem is a little bit more complicated than problem 5, but essentially we are performing the same operations.
Time complexity of creating a trie is O(n*m), where n is the number of path parts and m the average length of paths (length in number of path parts, not number of characters). Insertions and lookups have the same complexity.
Other than that, we are splitting the paths with the split built-in function, which has O(n) complexity.
## Space complexity
Space complexity would also be O(n*m), which gives an upper bound, because it does not consider common prefixes.