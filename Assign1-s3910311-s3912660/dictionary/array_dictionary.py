from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        self.dict = dict


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        dictionary = []

        #adds elements to array
        for x in words_frequencies:
            dictionary.append(x)

        #bubble sort dictionary alphabetically
        n = len(dictionary)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if dictionary[j].word > dictionary[j+1].word:
                    swapped = True
                    dictionary[j], dictionary[j+1] = dictionary[j+1],dictionary[j]

        self.dict = dictionary

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        #call dictionary to put into a variable
        dictionary = self.dict

        #iterate through all the list until we find the searched word
        for x in dictionary:
            if x.word == word:
                return x.frequency       

        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        dictionary = self.dict

        #set the word_stop to be the index for alphabetical order
        for x in dictionary:
            if x.word == word_frequency.word:
                word_stop = 0
                break
            elif word_frequency.word > x.word:
                word_stop = x
                
        #word is added if it is not found in the dictionary
        if word_stop == 0:
            return False
        else:       
            dictionary.insert(dictionary.index(word_stop) + 1,word_frequency) 
            return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        dictionary = self.dict

        #set the word_stop to be the index where we find a word
        for x in dictionary:
            if word == x.word:
                word_stop = x
                break
            else:
                word_stop = 0
            
        #remove word if it is found 
        if word_stop == 0:
            return False
        else:       
            dictionary.remove(word_stop) 
            return True


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        dictionary = self.dict
        prefix_list = []

        #add all words that start with the prefix into a list
        for x in dictionary:
            if x.word.startswith(prefix_word):
                prefix_list.append(x)

        n = len(prefix_list)
        swapped = False
        #sort the list from highest frequency to lowest
        for i in range(n-1):
            for j in range(0, n-i-1):
                if prefix_list[j].frequency < prefix_list[j+1].frequency:
                    swapped = True
                    prefix_list[j], prefix_list[j+1] = prefix_list[j+1],prefix_list[j]
                
        #keep the top 3 frequencies of the list
        prefix_list = prefix_list[:3]

        return prefix_list
