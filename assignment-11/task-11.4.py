class Node:
    """
    An object for storing a single node of a binary search tree.
    Models three attributes: data, and links to the left and right child nodes.
    """
    def __init__(self, data):
        """
        Initializes a Node instance.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A class representing a Binary Search Tree (BST).
    """

    def __init__(self):
        """
        Initializes an empty Binary Search Tree.
        The root is initialized to None.
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the correct position in the BST.

        Args:
            data: The data for the new node.
        """
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        """Helper method to recursively insert a node."""
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(data, current_node.left)
        else:  # data >= current_node.data
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(data, current_node.right)

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the BST.

        Returns:
            A list of node values in sorted order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        """Helper method to recursively perform in-order traversal."""
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.data)
            self._inorder_recursive(current_node.right, result)


# Example Usage
if __name__ == "__main__":
    # Create a new Binary Search Tree
    bst = BinarySearchTree()

    # Insert elements into the BST
    print("Inserting values: 50, 30, 70, 20, 40, 60, 80")
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for value in values_to_insert:
        bst.insert(value)

    # Perform an in-order traversal
    # This should print the elements in sorted order
    sorted_list = bst.inorder_traversal()
    print(f"\nIn-order traversal (sorted order): {sorted_list}")
    # Expected: [20, 30, 40, 50, 60, 70, 80]

    print("\nVerifying the sorted output:")
    print(f"Is the list sorted? {sorted_list == sorted(values_to_insert)}")
