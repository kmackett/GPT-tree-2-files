import os

# Read the input file and return the lines
def read_input_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return lines

# Construct the expected directory structure based on the input file lines
def construct_expected_structure(lines):
    expected_structure = []
    stack = [(lines[0].rstrip('\n'), -1)]

    # Iterate through the lines in the input file
    for line in lines[1:]:
        # Calculate the depth of the current line (number of leading spaces)
        depth = len(line) - len(line.lstrip(' │'))

        # Pop items from the stack until an item with a lower depth is found
        while stack and depth <= stack[-1][1]:
            stack.pop()

        # Extract the current item name
        item = line.lstrip(' │└├──').rstrip('\n')
        # Build the current item path
        current_path = stack[-1][0] + item

        # Determine if the current item is a directory or a file
        _, ext = os.path.splitext(item)
        is_directory = item.endswith('/') or (not ext and item != '.env')

        # If the current item is a directory
        if is_directory:
            # Ensure the item and current_path end with '/'
            if not item.endswith('/'):
                item += '/'
                current_path += '/'
            # Add the current item to the stack
            stack.append((current_path, depth))

        # Add the current item path to the expected structure
        expected_structure.append(current_path)
    
    return expected_structure

# Check the actual directory structure against the expected structure and return any missing items
def check_directory_structure(expected_structure):
    missing_items = []

    for item in expected_structure:
        if not os.path.exists(item):
            missing_items.append(item)
    
    return missing_items

# Main function
def main():
    input_file = "tree-directory-structure-in.txt"
    lines = read_input_file(input_file)
    expected_structure = construct_expected_structure(lines)
    missing_items = check_directory_structure(expected_structure)

    if missing_items:
        print("Missing items:")
        for item in missing_items:
            print(item)
    else:
        print("The directory structure matches the expected structure.")

if __name__ == "__main__":
    main()


'''
function read_input_file(input_file):
    read input_file into lines
    return lines

function construct_expected_structure(lines):
    initialize expected_structure and stack with the root directory

    for each line in lines starting from the second line:
        calculate depth as the number of leading spaces

        pop items from stack until an item with a lower depth is found

        extract the current item from line
        build current_path using the top item in stack and current item

        determine if current item is a directory or a file

        if current item is a directory:
            ensure current_path and item end with '/'
            add (current_path, depth) to stack

        add current_path to expected_structure

    return expected_structure

function check_directory_structure(expected_structure):
    initialize missing_items as an empty list

    for each item in expected_structure:
        if item does not exist in the file system:
            add item to missing_items

    return missing_items

function main:
    read the input file
    construct the expected directory structure
    check the actual directory structure against the expected structure
    report any missing items

'''