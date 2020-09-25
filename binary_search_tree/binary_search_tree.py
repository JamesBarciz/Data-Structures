"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # RECURSIVE
        if self.value is not None:
            if value < self.value:
                # if left child is None:
                if self.left is None:
                    self.left = BSTNode(value)  # add here
                else:
                    self.left.insert(value)  # recursive call
            elif value >= self.value:
                # if right child is None:
                if self.right is None:
                    self.right = BSTNode(value)  # add here
                else:
                    self.right.insert(value)  # recursive call
        else:
            self.value = value

        # ITERATIVE
        # while not at bottom level of tree
            # if value < root
                # if left child is None
                    # add here
                    # exit loop
            # if value >= root
                # if right child is None
                    # add here
                    # exit loop

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False            
            else:
                return self.right.contains(target)

        # # check if self.value is target
        # if target == self.value:
        #     # if yes, return true
        #     return True
        # elif self.value is None:
        #     return False
        # else: # if no
        #     # go left?
        #     if target < self.value:
        #         self.left.contains(target)
        #     # go right?
        #     elif target >= self.value:
        #         self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you cannot anymore
        # recursive / iterative
        if self.right is None:
            return self.value
        else:
            ptr = self.right
            while ptr.right is not None:
                ptr = ptr.right
            # return value at far right
            return ptr.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # one side then the other - fn(value)

        # Recursive
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        
        # Iterative
        # arr = [self]
        # while len(arr) > 0:
        #     node = arr.pop()
        #     fn(node.value)
        #     if node.left is not None:
        #         arr.append(node.left)
        #     if node.right is not None:
        #         arr.append(node.right)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Recursive: place print statement in between
        # recursive calls that explore left and right subtrees
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()
        # OR
        # Iterative - think about the order in which we are
        # adding nodes to the stack
        # stack = []
        # while len(stack) >= 0:
        #     node = self
        #     if node.right is not None:
        #         stack.append(node.right)
        #     stack.append(node)
        #     if node.left is not None:
        #         stack.append(node.left)
        # return stack
            


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a QUEUE to keep track of nodes we are procesing
        # add 'self' to front of queue
        arr = [self]
        while len(arr) > 0:
            node = arr.pop()
            print(node.value)
            if node.left is not None:
                arr.insert(0, node.left)
            if node.right is not None:
                arr.insert(0, node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        arr = [self]
        while len(arr) > 0:
            node = arr.pop()
            print(node.value)
            if node.left is not None:
                arr.append(node.left)
            if node.right is not None:
                arr.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
