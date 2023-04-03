# Python3 program to convert a left
# unbalanced BST to a balanced BST


# A binary tree node has data, pointer to left child
# and a pointer to right child
class BinarySearchNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = self.__right = None

    def data(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def left(self):
        return self.__left

    def setLeft(self, left):
        self.__left = left

    def right(self):
        return self.__right

    def setRight(self, right):
        self.__right = right

    # This function traverse the skewed binary tree and
    # stores its nodes pointers in vector nodes[]
    def __storeBSTNodes(self, nodes):
        # Base case
        if not self:
            return

        # Store nodes in Inorder (which is sorted
        # order for BST)
        if self.left() is not None:
            self.left().__storeBSTNodes(nodes)
        nodes.append(BinarySearchNode(self.data()))
        if self.right() is not None:
            self.right().__storeBSTNodes(nodes)

    # Recursive function to construct binary tree
    def __buildTreeUtil(self, nodes, start, end):
        # base case
        if start > end:
            return None

        # Get the middle element and make it root
        mid = (start + end) // 2
        node = nodes[mid]

        # Using index in Inorder traversal, construct
        # left and right subtrees
        node.setLeft(self.__buildTreeUtil(nodes, start, mid - 1))
        node.setRight(self.__buildTreeUtil(nodes, mid + 1, end))
        return node

    # This functions converts an unbalanced BST to
    # a balanced BST
    def balance(self):
        # Store nodes of given BST in sorted order
        nodes = []
        self.__storeBSTNodes(nodes)

        # Constructs BST from nodes[]
        n = len(nodes)
        return self.__buildTreeUtil(nodes, 0, n - 1)

    def has(self, data):
        print(self.data())
        print(data)
        if self.data() is None:
            return False
        elif self.data() == data:
            return True
        elif self.data() < data:
            if self.right() is None:
                return False
            else:
                return self.right().has(data)
        else:
            if self.left() is None:
                return False
            else:
                return self.left().has(data)

    def insert(self, data):
        if self.data() is None:
            self.setData(data)
        elif self.data() < data:
            if self.right() is None:
                self.setRight(BinarySearchNode(data))
            else:
                self.right().insert(data)
        elif self.data() > data:
            if self.left() is None:
                self.setLeft(BinarySearchNode(data))
            else:
                self.left().insert(data)


# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
    if len(arr) == 0:
        return None

    # find middle
    mid = (len(arr)) // 2

    # make the middle element the root
    root = BinarySearchNode(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root
