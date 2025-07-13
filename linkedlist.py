class Node:
    '''
    A class to create a linkedlist node \n
    input: Pass data value \n
    output: None returned; object is created and can be accessed
    '''
    def __init__(self, data):
        self.data = data # assigns the data to the node
        self.next = None # sets the next pointer to None initially

class LinkedList:
    """
    Description: A class to initialize the linked list and be utilized to perform certain basic operations.\n
    Functions available:\n
    \t 1.\t insertAtBeginning(data)
    \t 2.\t printList()
    \t 3.\t insertAtLast(data)
    \t 4.\t deleteFromBeginning()
    """
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        """
        Description: Function to insert the data at the start of the linked list. \n
        Input: new data to be inserted. \n
        Output: None; Linked list is altered\n
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        """
        Description: Function to display all the data inside the linked list \n
        Input: None \n
        Output: None; Linked list is printed \n
        """
        list_len = 0
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
            list_len += 1
        print()
        return list_len

    def insertAtLast(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            # self.insertAtBeginning(new_data)
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insertAtPosition(self, new_data, position):
        """
        example: 1->2->3->4->5->6->7->8->9
        """
        new_node = Node(new_data)
        if position == 1:
            self.insertAtBeginning(new_data)
            return
        current_node = self.head
        for _ in range(position - 2):
            if current_node is None:
                break
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        return
    
    def deleteFromBeginning(self):
        if self.head is None:
            return "The Linked List is empty"
        self.head = self.head.next

    def deleteitem(self, value):
        if self.head is None:
            return "The Linked List is empty"

        # Delete all occurrences at the head
        while self.head is not None and self.head.data == value:
            self.head = self.head.next

        # Delete occurrences after the head
        current = self.head
        while current is not None and current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next
        return
        

if __name__ == "__main__":
    llist = LinkedList()

    llist.insertAtBeginning('fox')
    llist.insertAtBeginning('brown')
    llist.insertAtBeginning('quick')
    llist.insertAtBeginning('the')

    llist.insertAtLast("jumps")

    llist.printList()

    llist.insertAtPosition("arsenal", 2)
    print(llist.printList())
    llist.deleteitem("arsenal")
    print(llist.printList())
    