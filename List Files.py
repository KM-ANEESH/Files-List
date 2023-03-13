import os
from_dir = "C:/Users/karan/Desktop"
list_files = os.listdir(from_dir)
print (list_files)
for file_name in list_files:
    print(file_name)
    root,exe =  os.path.splitext(file_name)
    print(root)
    print(exe)