# Windows file path: C:\path\to\file.txt
# Linux file path  : /path/to/file.txt

import os

print('C:\\path\\to\\file.txt')
print('/path/to/file.txt')
print(r'C:\path\to\file.txt')

# os.path.join will generate OS-independent path string
print(os.path.join('path', 'to', 'file.txt'))
print('Separator character: ' + os.sep)

print('==============================')

# os.getcwd() gets current working directory
home = os.getcwd()
print('Current working directory: ' + os.getcwd())

# os.chdir changes current working directory
os.chdir('/home/')
print('Current working directory: ' + os.getcwd())
os.chdir('..')
print('Current working directory: ' + os.getcwd())

# os.path.abspath() gets absolute path from a relative path
os.chdir(home)
print(os.path.abspath('file.txt'))

# os.path.isabs() checks whether absolute path
abspath = os.path.abspath(os.path.join('..', 'file.txt'))
print(abspath)
print(str(os.path.isabs(abspath)))
print(str(os.path.isabs('../file.txt')))

# os.path.relpath() gets relative path from an absolute path
print(os.path.relpath(abspath))

print('==============================')

# os.path.dirname() gets directory parts
# os.path.basename() gets filename part
abspath = os.path.abspath('file.txt')
print(abspath)
print(os.path.dirname(abspath))
print(os.path.basename(abspath))
