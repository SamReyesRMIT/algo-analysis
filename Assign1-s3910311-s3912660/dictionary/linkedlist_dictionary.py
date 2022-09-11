from hashlib import new
from platform import node
from re import search
from sys import prefix
from typing import List
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# # ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):

        self.head = None #initialise head node

    def build_dictionary(self, words_frequencies: [WordFrequency]): 
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        # CREATE LINKED LIST FROM LIST OF WORDS
        cur_node = self.head

        for word in words_frequencies: 
            new_node = ListNode(word)
            if self.head:
                cur_node = self.head
                while(cur_node.next):
                    cur_node = cur_node.next
                cur_node.next = new_node
            else:
                self.head = new_node


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
 
        item = self.head
        while item != None:
            if item.word_frequency.word == word:
                return item.word_frequency.frequency
            else:
                item = item.next
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        if self.search(word_frequency.word) == 0:
            new_node = ListNode(word_frequency)
            if self.head:
                cur_node = self.head
                while(cur_node.next):
                    cur_node = cur_node.next
                cur_node.next = new_node
            else:
                self.head = new_node
            return True
        else:
            return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        if self.head == None:
            return False

        cur_node = self.head
        prev_node = None

        if cur_node.word_frequency.word == word:
            self.head = cur_node.next
            return True

        prev_node = cur_node
        cur_node = cur_node.next

        while cur_node:
            if cur_node.word_frequency.word == word:
                prev_node.next = cur_node.next
                cur_node = None
                return True
            prev_node = cur_node
            cur_node = cur_node.next
        return False

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        
        output = []

        # APPENDS MATCHING WORDS TO ARRAY
        item = self.head
        while item != None:
            if item.word_frequency.word.startswith(word):
                output.append(item.word_frequency)
            item = item.next
        
        # SORT ARRAY
        output.sort(key=lambda x:x.frequency, reverse=True)
        
        # RETURNS TOP 3 WORDS   
        return output[:3]
       



