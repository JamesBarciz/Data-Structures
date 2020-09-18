"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def delete(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create new_node
        new_node = ListNode(value)
        # 1. empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node        
        # 2. not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        # update length
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # empty list
        if self.head is None:
            return
        else:
            ret_value = self.head.value
            # 1 item
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else: # 2+
                cur_node = self.head
                self.head = self.head.next
                cur_node.delete()
            self.length -= 1
            return ret_value


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # establish new_node
        new_node = ListNode(value)
        # empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # nonempty
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node        
        # update length
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # empty list
        if self.head is None:
            return
        else:
            ret_value = self.tail.value
            # 1 item
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                cur_node = self.tail
                self.tail = self.tail.prev
                cur_node.delete()
            self.length -= 1
            return ret_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # Iteration done somewhere else - just moving node
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # Iteration done somewhere else - just moving node
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Dont need to return value
        # Need to update head and tail
        # empty list
        if self.head is None:
            return None

        # list 1 item
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # list 2+ items
        elif node is self.head:
            self.head = node.next  # update head attribute
            node.delete()  # deal with prev and next ptr
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:             # middle
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # empty list
        if self.head is None:
            return None
        elif self.head == self.tail:
            return self.head.value
        else:
            l = []
            ptr = self.head
            while ptr is not None:
                l.append(ptr.value)
                ptr = ptr.next
            return max(l)
            # ptr1 = self.head
            # ptr2 = self.head.next
            # while not None:
            #     if ptr1.value > ptr2.value:
            #         ptr2 = ptr2.next
            #     elif ptr1.value < ptr2.value:
            #         ptr1 = ptr1.next
            #     else:
            #         ptr1 = ptr2.next
            # return (ptr1.value, ptr2.value)
