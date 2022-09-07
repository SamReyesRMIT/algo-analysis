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
        # TO BE IMPLEMENTED
        self.head = None

    def build_dictionary(self, words_frequencies: [WordFrequency]): 
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

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
#

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
        # # TO BE IMPLEMENTED
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:

        # add in a new element/adding a new node

        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        found = False

        item = self.head
        while item != None:
            if item.word_frequency.word == word_frequency.word:
                found = True
            else:
                item = item.next
                
        if found == False:
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

        
        # adding directly to the end of the linked
        # TO BE IMPLEMENTED

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
            

        # TO BE IMPLEMENTED
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        first = None
        second = None
        third = None

        output = []

        item = self.head
        while item != None:  #while item exists
            if item.word_frequency.word.startswith(word) and first != None and second != None:
                if first.frequency < item.word_frequency.frequency:
                    third = second
                    second = first
                    first = item.word_frequency
                elif second.frequency < item.word_frequency.frequency:
                    third = second
                    second = item.word_frequency
                elif second.frequency > item.word_frequency.frequency:
                    third = item.word_frequency
            elif item.word_frequency.word.startswith(word) and first == None: #if item starts with
                first = item.word_frequency
            elif item.word_frequency.word.startswith(word) and first != None:
                if first.frequency > item.word_frequency.frequency:
                    second = item.word_frequency
                else:
                    second = first
                    first = item.word_frequency

            item = item.next

        if first != None:
            output.append(first)
        if second != None:
            output.append(second)
        if third != None:
            output.append(third)
        
        # TO BE IMPLEMENTED
        return output



