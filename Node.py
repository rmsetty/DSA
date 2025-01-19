class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('empty')
            return
        itr = self.head
        x = ''
        while itr:
            x += str(itr.data)
            itr = itr.next
        print(x)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

    def insert_at_begining(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        #index < 0 or index >= self.getLength()
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                return
            count += 1
            itr = itr.next

    def remove_at(self, index):
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
        count += 1
        itr = itr.next        

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    itr = self.head
    while itr:
        if(itr.data == data_after):
            itr.next = Node(data_to_insert, itr.next)
        itr = itr.next
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
    itr = self.head
    while itr.next:
        if itr.next.data == data:
            itr.next = itr.next.next
            return
        itr = itr.next
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def print_forward(self):
    # This method prints list in forward direction. Use node.next
    itr = self.head
    x=''
    while itr:
        x += str(itr.data)
        itr = itr.next
    print(x)
        


def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
    itr = self.head
    x=''
    while itr:
        itr = itr.next
    while itr:
        x += str(itr.data)
        itr = itr.prev
    print(x)

