import argparse
import os

def process_directory_structure(input_file, create_structure=True, output_file=None, print_output=False):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    root_dir = lines[0].rstrip('\n')

    if root_dir == '.':
        root_dir = 'main'

    if not root_dir.endswith('/'):
        root_dir += '/'
    
    if print_output:
        print(root_dir)

    if output_file:
        with open(output_file, 'w') as out_file:
            out_file.write(root_dir + '\n')

    stack = [(root_dir, -1)]
    for line in lines[1:]:
        depth = len(line) - len(line.lstrip(' │'))
        while stack and depth <= stack[-1][1]:
            stack.pop()

        item = line.lstrip(' │└├──').rstrip('\n')
        current_path = stack[-1][0] + item

        _, ext = os.path.splitext(item)
        is_directory = item.endswith('/') or not ext

        if is_directory:
            if not item.endswith('/'):
                item += '/'
                current_path += '/'
            stack.append((current_path, depth))
            if create_structure:
                os.makedirs(current_path, exist_ok=True)
        else:
            if create_structure:
                with open(current_path, 'w') as _:
                    pass

        if print_output:
            print(current_path)
        if output_file:
            with open(output_file, 'a') as out_file:
                out_file.write(current_path + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert directory structure tree to full relative paths and create directories and files")
    parser.add_argument("-o", "--output", action="store_true", help="Create directory_structure_out.txt with the full relative paths")
    parser.add_argument("-p", "--print", action="store_true", help="Print directory structure to console")
    args = parser.parse_args()

    if args.output:
        output_file = "directory_structure_out.txt"
    else:
        output_file = None

    process_directory_structure("tree-directory-structure-in.txt", output_file=output_file, print_output=args.print)
