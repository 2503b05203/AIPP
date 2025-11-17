class Stack:
    """
    A simple Stack implementation using a Python list.

    This class provides the basic stack operations: push, pop, peek, and is_empty.
    It follows the Last-In, First-Out (LIFO) principle.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self._items.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If trying to pop from an empty stack.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If trying to peek at an empty stack.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self._items

    def __len__(self):
        """
        Returns the number of items in the stack.

        Allows using the built-in len() function on a Stack instance.
        """
        return len(self._items)

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return f"Stack({self._items})"


# Example Usage
if __name__ == "__main__":
    # Create a new stack
    my_stack = Stack()

    # Check if the stack is empty
    print(f"Is the stack empty? {my_stack.is_empty()}")  # Expected: True

    # Push items onto the stack
    print("Pushing 10, 20, 30...")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print(f"Current stack: {my_stack}")
    print(f"Stack size: {len(my_stack)}")

    # Peek at the top item
    print(f"Top item (peek): {my_stack.peek()}")  # Expected: 30

    # Pop an item from the stack
    print(f"Popped item: {my_stack.pop()}")  # Expected: 30
    print(f"Current stack after pop: {my_stack}")

    # Check if the stack is empty again
    print(f"Is the stack empty? {my_stack.is_empty()}")  # Expected: False

    # Pop remaining items
    print(f"Popped item: {my_stack.pop()}")  # Expected: 20
    print(f"Popped item: {my_stack.pop()}")  # Expected: 10

    # Check if the stack is empty
    print(f"Is the stack empty? {my_stack.is_empty()}")  # Expected: True
    print(f"Current stack: {my_stack}")

    # Demonstrate error handling
    try:
        my_stack.pop()
    except IndexError as e:
        print(f"Caught expected error: {e}")

