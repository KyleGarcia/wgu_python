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
            self.tail = new_node 

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node #setting new node to tail's next
            self.tail = new_node 
        else:
            new_node.next = current_node.next
            current_node.next = new_node

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

class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

num_list = LinkedList() #create an empty linked list

node_a = Node(95)
node_b = Node(42)
node_c = Node(60)
node_d = Node(70)

num_list.append(node_a)
num_list.append(node_b)
num_list.prepend(node_c)
num_list.insert_after(node_b, node_d)
num_list.remove_after(node_b)

# Traverse the List
current = num_list.head 
while current:
    print(current.data)
    current = current.next

