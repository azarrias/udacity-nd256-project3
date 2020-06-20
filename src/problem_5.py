## Represents a single node in the Trie
class TrieNode(object):
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes_list = []
        if self.is_word:
            if len(suffix) > 0:
                suffixes_list.append(suffix)
        for character, node in self.children.items():
            suffixes_list.extend(node.suffixes(suffix + character))
        return suffixes_list

## The Trie itself containing the root node and insert/find functions
class Trie(object):
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
    
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.insert(character)
            current_node = current_node.children[character]
        current_node.is_word = True
    
    def find(self, word):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for character in word:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return None
        return current_node

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
MyTrie = Trie()
n = ["empty", None]
result = MyTrie.find(n[0])
eval_test(1, n[0], n[1], result)

# test case 2
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
n = ["ant", ['hology', 'agonist', 'onym']]
prefix_node = MyTrie.find(n[0])
result = prefix_node.suffixes()
eval_test(2, n[0], n[1], result)

# test case 3
n = ["a", ['nt', 'nthology', 'ntagonist', 'ntonym']]
prefix_node = MyTrie.find(n[0])
result = prefix_node.suffixes()
eval_test(3, n[0], n[1], result)

# test case 4
n = ["fur", None]
result = MyTrie.find(n[0])
eval_test(4, n[0], n[1], result)

"""
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixNode = MyTrie.find("ant")
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
"""