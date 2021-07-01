import os

file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(file_path)
print(file_path)
print(dir_name)

# os.mkdir('path to dir')
# os.rmdir('path to dir')