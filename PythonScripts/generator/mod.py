import os


dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(dir_name)
s = dir_name + "/TextData"
print(s)
