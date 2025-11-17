number=[1,2,3]
try:
    index = 5
    if index < len(number):
        print(number[index])
    else:
        print(f"Error: Index {index} is out of range for list of length {len(number)}.")
except IndexError:
    print("Error: List index out of range.")