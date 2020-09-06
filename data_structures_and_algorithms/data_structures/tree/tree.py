class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        method to check if Queue is empty
        """
        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        """
        Method that takes any value as an argument and adds a new node with that value to the back of the queue:
            inp ---> value
        """
        new_node = node

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Method that removes the node from the front of the queue, and returns the node’s value:
            out >> the dequeueed value
        """
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """
        Method that returns the value of the node located in the front of the queue, without removing it from the queue:
            out >> the front value
        """
        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    def __init__(self):
        self._root = None

    def pre_order(self, node=None, arr = None):
        """
        Method to return an array of trre values in "pre-order" order:
            out >> list contain tree values in pre-order..
        """
        if arr is None:
            arr = []

        node = node or self._root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)

        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def in_order(self, node=None, arr = None):
        """
        Method to return an array of tree values "in-order" :
            out >> list contain tree values in-order..
        """
        if arr is None:
            arr = []

        node = node or self._root

        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)

        return arr

    def post_order(self, node=None, arr = []):
        """
        Method to return an array of tree values "post-order":
            out >> list of tree values in post-order..
        """
        node = node or self._root

        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr

    
class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Method that accepts a value, and adds a new node with that value in the correct location in the binary search tree:
            inp ---> value to be added to binry search tree
        """
        node = _Node(value)
        if not self._root:
            self._root = node
            return

        current = self._root
        while True:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return


    def contains(self,value):
        """
        lets cheack if you value is in the tree.. :)
        this method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once:
            inp ---> value to cheack if it is in the tree
            out >> boolean if the value in or not..
        """
        if self._root == None:
            raise "Tree is empty"

        current = self._root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False
