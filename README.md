# GPT-tree-2-files

GPT-tree-2-files is an open-source Python script that simplifies the process of creating directories and files based on a tree structure provided by ChatGPT. By using this script, you can automatically generate the required directories and empty files for your project, saving time and effort.

## Usage

1. Save the tree structure generated by ChatGPT into a file named `tree-directory-structure-in.txt` in the same directory as the `create_directory_structure.py` script.
2. Run the script using the following command:

python create_directory_structure.py


This will create the directory structure and empty files based on the tree structure provided in the `tree-directory-structure-in.txt` file.

### Optional flags

- `-o` or `--output`: Creates a file named `directory_structure_out.txt` containing the full relative paths of the directories and files.
- `-p` or `--print`: Prints the directory structure to the console.

For example, to create the directory structure, save the full relative paths to a file, and print the structure to the console, run:

python create_directory_structure.py -o -p


## License

GPT-tree-2-files is open-sourced under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as needed.
