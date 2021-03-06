# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path_part in path_list:
            if path_part not in current_node.children:
                current_node.insert(path_part)
            current_node = current_node.children[path_part]
        current_node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path_part in path_list:
            if path_part in current_node.children:
                current_node = current_node.children[path_part]
            else:
                return None
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        # Insert the node as before
        self.children[path_part] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        return self.route_trie.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        return self.route_trie.find(path_list)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        # return only parts of the path that are not empty or None
        return [part for part in path.split("/") if part]

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

router = Router("root handler")
router.add_handler("/home/about", "about handler")
router.add_handler("/home/blog", "blog handler")

# test case 1
n = ["/", "root handler"]
result = router.lookup(n[0])
eval_test(1, n[0], n[1], result)

# test case 2
n = ["/home", None]
result = router.lookup(n[0])
eval_test(2, n[0], n[1], result)

# test case 3
n = ["/home/about", "about handler"]
result = router.lookup(n[0])
eval_test(3, n[0], n[1], result)

# test case 4
n = ["/home/blog", "blog handler"]
result = router.lookup(n[0])
eval_test(4, n[0], n[1], result)

# test case 5
n = ["/home/about/me", None]
result = router.lookup(n[0])
eval_test(5, n[0], n[1], result)

"""
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
#router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
"""