import argparse
import os

# Function that processes the input file and creates the directory structure
def process_directory_structure(input_file, create_structure=True, output_file=None, print_output=False):
    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extract the root directory
    root_dir = lines[0].rstrip('\n')

    # If the root directory is '.', use 'main' as the root directory
    if root_dir == '.':
        root_dir = 'main'

    # Ensure the root directory ends with '/'
    if not root_dir.endswith('/'):
        root_dir += '/'
    
    # Print the root directory if the print_output flag is set
    if print_output:
        print(root_dir)

    # Write the root directory to the output file if specified
    if output_file:
        with open(output_file, 'w') as out_file:
            out_file.write(root_dir + '\n')

    # Initialize the stack with the root directory
    stack = [(root_dir, -1)]
    
    # Iterate through the lines in the input file (ignoring the first line, which is the root directory)
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
            # Create the directory if the create_structure flag is set
            if create_structure:
                os.makedirs(current_path, exist_ok=True)
        else:
            # Create the file if the create_structure flag is set
            if create_structure:
                with open(current_path, 'w') as _:
                    pass

        # Print the current item path if the print_output flag is set
        if print_output:
            print(current_path)

        # Write the current item path to the output file if specified
        if output_file:
            with open(output_file, 'a') as out_file:
                out_file.write(current_path + '\n')

# Main function
if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Convert directory structure tree to full relative paths and create directories and files")
    parser.add_argument("-o", "--output", action="store_true", help="Create directory_structure_out.txt with the full relative paths")
    parser.add_argument("-p", "--print", action="store_true", help="Print directory structure to console")
    args = parser.parse_args()

    # Determine the output file name
    if args.output:
        output_file = "directory_structure_out.txt"
    else:
        output_file = None

    # Call the process_directory_structure function with the appropriate arguments

        process_directory_structure("tree-directory-structure-in.txt", output_file=output_file, print_output=args.print)

   
'''
pseudocode for the logic used in the process_directory_structure function:

function process_directory_structure(input_file, create_structure, output_file, print_output):
    read input_file into lines

    set root_dir as the first line in lines
    if root_dir is '.', set root_dir to 'main'
    ensure root_dir ends with '/'

    if print_output, print root_dir
    if output_file, write root_dir to output_file

    initialize stack with (root_dir, -1)

    for each line in lines starting from the second line:
        calculate depth as the number of leading spaces

        pop items from stack until an item with a lower depth is found

        extract the current item from line
        build current_path using the top item in stack and current item

        determine if current item is a directory or a file

        if current item is a directory:
            ensure current_path and item end with '/'
            add (current_path, depth) to stack
            if create_structure, create the directory at current_path
        else:
            if create_structure, create the file at current_path

        if print_output, print current_path
        if output_file, write current_path to output_file

'''