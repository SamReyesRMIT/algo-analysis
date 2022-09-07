import bisect
from re import search
from threading import currentThread

array = []
class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None


array.append(WordFrequency("cute",100))
array.append(WordFrequency("ant",20))
array.append(WordFrequency("cut",30))
array.append(WordFrequency("cuts",50))
array.append(WordFrequency("cutter",90))
array.append(WordFrequency("cutting",800))

head = None

cur_node = head

for word in array:
    new_node = ListNode(word)
    if head:
        cur_node = head
        while(cur_node.next):
            cur_node = cur_node.next
        cur_node.next = new_node
    else:
        head = new_node


print (head.next.word_frequency.word)


first = None
second = None
third = None

prefix = 'cut'

# SEARCH FOR WORDS
item = head
while item != None:  #while item exists
    if item.word_frequency.word.startswith(prefix) and first != None and second != None:
        if first.frequency < item.word_frequency.frequency:
            third = second
            second = first
            first = item.word_frequency
        elif second.frequency < item.word_frequency.frequency:
            third = second
            second = item.word_frequency
        elif second.frequency > item.word_frequency.frequency:
            third = item.word_frequency
    elif item.word_frequency.word.startswith(prefix) and first == None: #if item starts with prefix
        first = item.word_frequency
    elif item.word_frequency.word.startswith(prefix) and first != None:
        if first.frequency > item.word_frequency.frequency:
            second = item.word_frequency
        else:
            second = first
            first = item.word_frequency

    item = item.next
print (first.word, second.word, third.word)




# if current node.WordFrequency.word has the prefix == True
#     compare node.WordFrequency.frequency with first,second,third 
#     set values for first second third
#     return first second third
