class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, data):
        new_node= Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next= new_node
            self.tail = new_node
    def dequeue(self, data):
        if self.head is None:
            return None
        data = self.head.data
        self.head= self.head.next
        if self.head is None:
            self.tail = None
        return data
    def size(self):
        current = self.head
        count =0
        while current:
            count+=1
            current = current.next
        return count
data_number = Queue()
data_number.enqueue(1)
data_number.enqueue(3)
data_number.enqueue(4)
data_number.enqueue(5)
print(data_number.enqueue(6))
print(data_number.dequeue(1))
print(data_number.size())

class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)
    def pop(self):
        if not self.empty():
            return self.container.pop()
    def size(self):
        return len(self.container)
    def insert(self, item, position):
        if position ==0:
            self.container.insert(0,item)
        elif position >0 and position<self.size():
            self.container.insert(position, item)
        else:
            self.container.append(item)
    def delete(self, item):
        if item in self.container:
            self.container.remove(item)
    def search(self, item):
        if item in self.container:
            return self.container.index(item)
stack1 = Stack()
stack1.insert(3,1)
stack1.insert(2,2)
stack1.insert(2,4)
print(stack1.search(1))
stack1.insert(2,7)
stack1.insert(1,5)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_head(self):
        if self.head is None:
            return
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next
    def delete_at_tail(self):
        current_node = self.head
        if self.head is None:
            return
        if current_node.next is None:
            self.head= None
            return
        while current_node.next:
            current_node = current_node.next
        current_node.next.prev = None
    def insert_at_head(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def insert_at_tail(self, item):

        if self.head is None:
            self.head = Node(item)
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(item)
        curr_node.next.prev = curr_node
    def search(self, key):
        curr_node= self.head
        while curr_node:
            if curr_node.data ==key:
                return True
            curr_node = curr_node.next
        return False

db_1 = DoubleLinkedList()
print(db_1.insert_at_head(2))
print(db_1.insert_at_tail(45))
print(db_1.search(45))

from abc import ABC, abstractmethod
class Operations(ABC):
    @abstractmethod
    def calculate(self):
        pass
class Add(Operations):
    def calculate(self, n1,n2):
        return n1+n2

class Sub(Operations):
    def calculate(self, n1,n2):
        return n1-n2
class Division(Operations):
    def calculate(self, n1, n2):
        return n1//n2
class Multiply(Operations):
    def calculate(self, n1,n2):
        return n1*n2
class OperartionFactory:
    @staticmethod
    def get_operation(op, n1,n2):
        if op=="+":
            return Add()
        elif op=="-":
            return Sub()
        elif op =="*":
            return Multiply()
        else:
            return Division()

add_op = OperartionFactory.get_operation("+",3,4)
print(add_op.calculate(3,4))
sub = OperartionFactory.get_operation("-", 9,3)
print(sub.calculate(9,3))
# mul = Multiply()
# print(add_op.calculate(3,5))
# print(sub.calculate(5,6))
# print(mul.calculate(5,6))

class GoogleDoc:
    def request(self):
        return "Please request access"
class Proxy:
    def __init__(self):
        self.doc = GoogleDoc()
    def request(self):
        return self.doc.request()
proxy = Proxy()
print(proxy.request())