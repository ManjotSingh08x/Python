class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Llist:
    def __init__(self):
        self.head = None
    
    def InsertAtBeginning(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def InsertAtIndex(self, data, index):
        counter = 1
        
        
e