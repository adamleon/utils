import os

print("Hello World")

num_spaces = 4
folder_symbol = "--[ "
file_symbol = "-- "

def print_folder(folder, files, level = 0):
    indent = level * (num_spaces * ' ')
    print(indent + folder_symbol + folder)
    indent = indent + ((num_spaces - 1) * ' ') + '|'

    for file in files:
        print(indent + file_symbol + file)


folderA = "test_folder"
subfoldersA = ["folder_A", "folder_B" , "folder_C", "folder_D"]
filesA = ["file_A.py", "file_B.py", "file_C.py"]

print_folder(folderA, filesA)

for root, dirs, files in os.walk(os.getcwd()):
    print_folder(root, files)