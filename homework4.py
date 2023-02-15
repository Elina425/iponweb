
# TASK 1
# Create a class that implements a binary search tree and can perform basic
# operations such as insertion, deletion, and searching.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        parent = None
        current = self.root
        while current is not None:
            if value == current.value:
                if current.left is None and current.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    return
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    return
                else:
                    successor = current.right
                    while successor.left is not None:
                        successor = successor.left
                    current.value = successor.value
                    value = successor.value
                    parent = current
                    current = current.right
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return False
bst = BST()
bst.insert(5)
bst.insert(2)
bst.insert(7)
bst.insert(1)
bst.insert(3)

print(bst.search(5))
print(bst.search(4))

bst.delete(2)
print(bst.search(2))

#Task2
#Red-black tree

class Node:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if not self.root:
            self.root = Node(value, color='black')
            return

        node = self.root
        while True:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(value, parent=node)
                    self._insert_fixup(node.left)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(value, parent=node)
                    self._insert_fixup(node.right)
                    break

    def delete(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.nil:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.nil:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'BLACK':
            self.delete_fixup(x)

    def delete_fixup(self, node):
        while node != self.root and node.color == 'BLACK':
            if node == node.parent.left:
                w = node.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.left_rotate(node.parent)
                    w = node.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    node = node.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = node.parent.right
                    w.color = node.parent.color
                    node.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                w = node.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    node.parent.color = 'RED'
                    self.right_rotate(node.parent)
                    w = node.parent.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    node = node.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = node.parent.left
                    w.color = node.parent.color
                    node.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 'BLACK'

    def search(self, value):
        node = self._search(value)
        return node is not None

    def _minimum(self, node):
        while node.left:
            node = node.left
        return node

    def _search(self, value):
        node = self.root
        while node and node.value != value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def _insert_fixup(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'red'
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(15)
rbt.delete(13)
rbt.search(10)

# TASK 3
# Write a function that implements a merge sort algorithm.
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array
print(merge_sort( [38, 27, 43, 3, 9, 82, 10]))

# TASK 4
# Write a function that implements an insertion sort algorithm.
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
print(insertion_sort( [38, 27, 43, 3, 9, 82, 10]))

# TASK 5
# Write a function that implements a sorting algorithm in linear time.
def counting_sort(array):
    n = len(array)
    count = {}

    for i in range(n):
        if array[i] in count:
            count[array[i]] += 1
        else:
            count[array[i]] = 1

    index = 0
    for key in sorted(count.keys()):
        for j in range(count[key]):
            array[index] = key
            index += 1

    return array
print(counting_sort( [38, 27, 43, 3, 9, 82, 10]))

