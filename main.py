class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.prev = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

    def append(self, new_node):
        if self.head == None:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail 
            self.tail = new_node 

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node #setting new node to tail's next
            new_node.prev = self.tail
            self.tail = new_node 
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node

    def remove_after(self, current_node):
        # Special case, remove head
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node == None:
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:
                self.tail = current_node

    def remove(self, current_node):
        successor_node = current_node.next
        predecessor_node = current_node.prev

        if successor_node is not None:
            successor_node.prev = predecessor_node
        if predecessor_node is not None:
            predecessor_node.next = successor_node
        if current_node is self.head:
            self.head = successor_node
        if current_node is self.tail:
            self.tail = predecessor_node




num_list = LinkedList() #create an empty linked list

node_a = Node(1)
node_b = Node(2)
node_c = Node(3)
node_d = Node(4)
node_e = Node(5)

num_list.append(node_a)
num_list.append(node_b)
num_list.append(node_c)
num_list.prepend(node_d)
num_list.insert_after(node_a, node_e)
num_list.remove(node_c)

# Traverse the List
current = num_list.head 
while current:
    print(current.data)
    current = current.next

