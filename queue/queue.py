"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         '''Add a new value to the queue'''
#         self.storage.insert(0, value)
#         self.size += 1

#     def dequeue(self):
#         '''Remove first value from queue'''
#         if self.size == 0:
#             return None
#         else:
#             last_val = self.storage[-1]
#             self.storage.pop()
#             self.size -= 1
#             return last_val


import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


from singly_linked_list.singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        '''Add a new value to the queue'''
        '''Head of linked list'''
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        '''Remove first value from queue'''
        '''Tail of linked list'''
        self.size -= 1
        if self.size < 0:
            self.size = 0
        return self.storage.remove_tail()
