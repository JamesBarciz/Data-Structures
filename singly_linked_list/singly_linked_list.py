class Node:
    """Node class for a Linked List"""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    """Save a reference to the head and tail"""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node        
        # 2. LL is not empty
        else:
            # update fmr tail to point to new node
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # Consider:
        # empty list
        if self.head is None:
            return None
        # else: return value of fmr head
        else:
            ret_value = self.head.get_value()
            # list of length 1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list of length 2+
            else:
                self.head = self.head.get_next_node()
        return ret_value


    def remove_tail(self):
        # empty list
        if self.tail is None:
            self.head = None
            return None
        else:
            # fmr tail value
            ret_value = self.tail.get_value()
            # list of length 1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list of length 2+
            else:
                second_last = self.head
                while second_last.get_next_node() != self.tail:
                    second_last = second_last.get_next_node()
                second_last.set_next_node(None)
                self.tail = second_last
            return ret_value

    def contains(self, value):
        # loop through LL until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next_node()
        return False

    def get_max(self):
        ptr1 = self.head
        l = []
        if ptr1 is None:
            return None
        else:
            # while loop
            while ptr1 != self.tail:
                # keep track of the biggest value as you iterate
                l.append(ptr1.get_value())
                ptr1 = ptr1.get_next_node()
            l.append(self.tail.get_value())
            # return biggest value
            return max(l)
