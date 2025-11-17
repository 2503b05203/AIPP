class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes: data and the link to the next node in the list.
    """
    def __init__(self, data):
        """
        Initializes a Node instance.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        The head is initialized to None.
        """
        self.head = None

    def insert_at_end(self, data):
        """
        Inserts a new node with the given data at the end of the list.

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        """
        Inserts a new node with the given data at the beginning of the list.

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """
        Displays all the elements of the linked list in a readable format.
        The format is "data1 -> data2 -> ... -> None".
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements) + " -> None")


# Example Usage
if __name__ == "__main__":
    # Create a new singly linked list
    sll = SinglyLinkedList()

    print("Initial list:")
    sll.display()  # Expected: -> None

    # Insert elements at the end
    print("\nInserting 10 and 20 at the end...")
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.display()  # Expected: 10 -> 20 -> None

    # Insert elements at the beginning
    print("\nInserting 5 and 0 at the beginning...")
    sll.insert_at_beginning(5)
    sll.insert_at_beginning(0)
    sll.display()  # Expected: 0 -> 5 -> 10 -> 20 -> None

    print("\nFinal list:")
    sll.display()  # Expected: 0 -> 5 -> 10 -> 20 -> None
