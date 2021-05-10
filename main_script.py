# https://www.geeksforgeeks.org/data-structures/

#----------------------------------------------------------------------------#
# A simple Python program for traversal of a linked list
# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

    # Function to insert a new node at the beginning O(1)
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

def run_linkedlist():
    # Head is initialised with a Node. Nodes have a class variable 'next' which
    # holds the next node (or None)
    print('-----LinkedList------')
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
    llist.push(0.5) # Insert new node at the start

    llist.printList()


if __name__=='__main__':
    run_linkedlist()