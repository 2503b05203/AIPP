def read_file(filename):
    """
    Reads data from a file safely.

    Args:
        filename (str): The path to the file.

    Returns:
        str: The content of the file, or None if an error occurs.
    """
    try:
        # The 'with' statement ensures the file is automatically
        # closed even if errors occur.
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None
