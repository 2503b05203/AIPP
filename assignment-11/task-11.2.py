class Queue:
    """
    A simple Queue implementation using a Python list.

    This class provides the basic queue operations: enqueue, dequeue, peek, and is_empty.
    It follows the First-In, First-Out (FIFO) principle.
    """

    def __init__(self):
        """Initializes an empty queue."""
        self._items = []

    def enqueue(self, item):
        """
        Adds an item to the back of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If trying to dequeue from an empty queue.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If trying to peek at an empty queue.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self._items

    def __len__(self):
        """
        Returns the number of items in the queue.

        Allows using the built-in len() function on a Queue instance.
        """
        return len(self._items)

    def __str__(self):
        """
        Returns a string representation of the queue.
        """
        return f"Queue({self._items})"


# Example Usage
if __name__ == "__main__":
    # Create a new queue
    my_queue = Queue()

    # Check if the queue is empty
    print(f"Is the queue empty? {my_queue.is_empty()}")  # Expected: True

    # Enqueue items into the queue
    print("Enqueuing 10, 20, 30...")
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    print(f"Current queue: {my_queue}")
    print(f"Queue size: {len(my_queue)}")

    # Peek at the front item
    print(f"Front item (peek): {my_queue.peek()}")  # Expected: 10

    # Dequeue an item from the queue
    print(f"Dequeued item: {my_queue.dequeue()}")  # Expected: 10
    print(f"Current queue after dequeue: {my_queue}")

    # Dequeue remaining items
    print(f"Dequeued item: {my_queue.dequeue()}")  # Expected: 20
    print(f"Dequeued item: {my_queue.dequeue()}")  # Expected: 30

    # Demonstrate error handling
    try:
        my_queue.dequeue()
    except IndexError as e:
        print(f"Caught expected error: {e}")