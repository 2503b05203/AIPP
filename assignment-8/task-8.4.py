# test_shopping_cart.py
import unittest

class ShoppingCart:
    """
    A simple shopping cart class to manage items.
    """
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}

    def add_item(self, name, price):
        """
        Adds an item with a name and price to the cart.
        Raises ValueError for invalid inputs.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(price, (int, float)):
            raise ValueError("Item price must be a number.")
        if price < 0:
            raise ValueError("Item price cannot be negative.")
        
        self.items[name] = price

    def remove_item(self, name):
        """
        Removes an item by name from the cart.
        Raises KeyError if the item is not found.
        """
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in cart.")
        del self.items[name]

    def total_cost(self):
        """Returns the total cost of all items in the cart."""
        return sum(self.items.values())

class TestShoppingCart(unittest.TestCase):
    """
    Test suite for the ShoppingCart class.
    """

    def setUp(self):
        """Set up a new, empty shopping cart before each test."""
        self.cart = ShoppingCart()

    # 1. Typical Scenarios
    def test_add_single_item_and_check_total(self):
        """Test adding one item and verifying the total cost."""
        self.cart.add_item("Apple", 0.5)
        self.assertEqual(self.cart.total_cost(), 0.5)

    def test_add_multiple_items_and_check_total(self):
        """Test adding multiple items and verifying the total cost."""
        self.cart.add_item("Apple", 0.5)
        self.cart.add_item("Banana", 0.75)
        self.cart.add_item("Orange", 0.6)
        self.assertAlmostEqual(self.cart.total_cost(), 1.85)

    def test_remove_item_and_check_updated_total(self):
        """Test removing an item and verifying the updated total cost."""
        self.cart.add_item("Milk", 3.0)
        self.cart.add_item("Bread", 2.5)
        self.cart.remove_item("Milk")
        self.assertEqual(self.cart.total_cost(), 2.5)

    # 2. Boundary Cases
    def test_add_item_with_zero_price(self):
        """Test adding an item with a price of 0."""
        self.cart.add_item("Freebie", 0)
        self.assertEqual(self.cart.total_cost(), 0)

    def test_add_item_with_negative_price_raises_error(self):
        """Test that adding an item with a negative price raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item("Discount", -10.0)

    def test_remove_item_not_in_cart_raises_error(self):
        """Test that removing an item not in the cart raises a KeyError."""
        self.cart.add_item("Apple", 0.5)
        with self.assertRaises(KeyError):
            self.cart.remove_item("Banana")

    # 3. Edge Cases
    def test_total_cost_of_empty_cart(self):
        """Test that the total cost of an empty cart is 0."""
        self.assertEqual(self.cart.total_cost(), 0)

    def test_remove_already_removed_item_raises_error(self):
        """Test that removing an item twice raises a KeyError on the second attempt."""
        self.cart.add_item("Book", 15.0)
        self.cart.remove_item("Book")
        with self.assertRaises(KeyError):
            self.cart.remove_item("Book")

    # 4. Invalid Inputs
    def test_add_item_with_non_string_name_raises_error(self):
        """Test that adding an item with a non-string name raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item(123, 1.0)
        with self.assertRaises(ValueError):
            self.cart.add_item(None, 1.0)
        with self.assertRaises(ValueError):
            self.cart.add_item([], 1.0)

    def test_add_item_with_non_numeric_price_raises_error(self):
        """Test that adding an item with a non-numeric price raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item("Apple", "one dollar")
        with self.assertRaises(ValueError):
            self.cart.add_item("Apple", None)
        with self.assertRaises(ValueError):
            self.cart.add_item("Apple", [])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
