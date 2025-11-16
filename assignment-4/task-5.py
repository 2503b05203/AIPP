import os

# task-5.py
# Function to count lines in '.txt' located in the same folder as this file.
# Few-shot examples (illustrative):
#   If sample.txt contains:
#     a
#     b
#   then count_lines_in_txt() -> 2
#
#   If .txt is empty then count_lines_in_txt() -> 0


def count_lines_in_txt() -> tuple:
    """Find the first .txt file in the same folder as this script and return (filename, line_count)."""
    base = os.path.dirname(__file__) or '.'
    # List all files in the folder
    try:
        files = os.listdir(base)
    except OSError as e:
        raise OSError(f"Could not list folder: {base}") from e
    
    # Find the first .txt file
    txt_files = [f for f in files if f.endswith('.txt')]
    if not txt_files:
        raise FileNotFoundError(f"No .txt files found in: {base}")
    
    # Use the first .txt file found
    txt_file = txt_files[0]
    path = os.path.join(base, txt_file)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            line_count = sum(1 for _ in f)
        return txt_file, line_count
    except FileNotFoundError:
        raise FileNotFoundError(f"'{txt_file}' not found at: {path}")

if __name__ == "__main__":
    try:
        # Find the first .txt file and print its name and line count
        filename, line_count = count_lines_in_txt()
        print(f"{filename} has {line_count} lines")
    except Exception as err:
        print("Error:", err)