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
