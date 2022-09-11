from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        # create the root node
        self.root = TrieNode("")

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # start from root node
        node = self.root

        # for every word
        for words in words_frequencies:
            #for each char in the word
            for char in words.word:
                # the node is create if it does not exist, or we traverse through the node
                if char in node.children:
                    node = node.children[char]
                else:
                    new_node = TrieNode(char)
                    node.children[char] = new_node
                    node = new_node
            # set is_last to true when the last character reached
            node.is_last = True
            node.frequency = words.frequency
            node = self.root


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # start from root node
        node = self.root

        # traverse throguh trie if the characters in search word are in the trie
        for char in word:
            if char in node.children:
                node = node.children[char] 
            else:
                return 0
            
        # return frequency if is_last is true
        if node.is_last == True:
            return node.frequency
        else:
            return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # start from root node
        node = self.root

        # traverse throguh trie and create nodes if the characters in add word are in the trie
        for char in word_frequency.word:
            if char in node.children:
                node = node.children[char] 
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                
        # create word from input 
        if node.is_last == True:
            return False
        else:
            node.is_last = True
            node.frequency = word_frequency.frequency
            return True


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # start from root node
        node = self.root

        # traverse throguh trie according to input word
        for char in word:
            if char in node.children:
                node = node.children[char] 
            else:
                break

        # set is_last to false if the word is found
        if node.is_last == True:
            node.is_last = False
            return True
        else:
            return False

    # dfs that shows found words while starting from a node
    def traverse(self,root, prefix, result, freq):
        if root.is_last:
            result.append(prefix[:])
            freq.append(root.frequency)
        for c,n in root.children.items():
            prefix.append(c)
            self.traverse(n, prefix, result,freq)
            prefix.pop(-1)

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        node = self.root
        # make the starting node to be the input word
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return []
        result = []
        frequency = []
        # add all the words found starting from the node of input
        self.traverse(node, list(word), result, frequency)
    
        output = []

        #parse words into a list
        words = [''.join(r) for r in result]

        # create the WordFrequency objects from the above traverse method
        for i in range(len(words)):
            output.append(WordFrequency(words[i], frequency[i]))
        
        # sort the list from highest frequency to lowest
        n = len(output)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if output[j].frequency < output[j+1].frequency:
                    swapped = True
                    output[j], output[j+1] = output[j+1],output[j]
                
        # keep top 3 frequency words
        output = output[:3]

        return output