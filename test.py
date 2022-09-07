import bisect
from re import search
from threading import currentThread

array = []
class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node

array.append(WordFrequency("cute",100))
array.append(WordFrequency("ant",20))
array.append(WordFrequency("cut",30))
array.append(WordFrequency("cuts",50))
array.append(WordFrequency("cutter",90))
array.append(WordFrequency("cutting",800))


root = TrieNode("")

node = root

for words in array:
    for char in words.word:
        if char in node.children:
            node = node.children[char]
        else:
            new_node = TrieNode(char)
            node.children[char] = new_node
            node = new_node
    node.is_last = True
    node.frequency = words.frequency
    node = root

search_word = "cutti"

node = root
for char in search_word:
    if char in node.children:
        node = node.children[char] 
    else:
        break
        
if node.is_last == True:
    print(node.frequency)
else:
    print("0")

add_word = WordFrequency("cutlery",69)

node = root
for char in add_word.word:
    if char in node.children:
        node = node.children[char] 
    else:
        new_node = TrieNode(char)
        node.children[char] = new_node
        node = new_node
        
if node.is_last == True:
    print("alr exist")
else:
    node.is_last = True
    node.frequency = add_word.frequency

delete_word = "cutlery"

node = root
for char in delete_word:
    if char in node.children:
        node = node.children[char] 
    else:
        break

if node.is_last == True:
    node.is_last = False
    print("true")
else:
    print("false")

'''        

node = root
word_AC = "cut"


for char in word_AC:
    if char in node.children:
        node = node.children[char]
    else:
        print(output) # or do nth

if node.is_last == True:
    output.append(WordFrequency(word_AC, node.frequency))

#traverse through the tree to get all the words

print(output)

'''


def traverse(root, prefix, result, freq):
    if root.is_last:
        result.append(prefix[:])
        freq.append(root.frequency)
    for c,n in root.children.items():
        prefix.append(c)
        traverse(n, prefix, result,freq)
        prefix.pop(-1)

def search(word):
    node = root
    for w in word:
        if w in node.children:
            node = node.children[w]
        else:
            return []
    result = []
    frequency = []
    traverse(node, list(word), result, frequency)
    return [''.join(r) for r in result], frequency

output = []

print(search("cut")[0])
print(search("cut")[1])       

for i in search("cut")[0]:
    output.append(Word)
    
