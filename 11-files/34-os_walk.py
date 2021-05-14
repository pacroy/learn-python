import os

# os.walk() iterate through each folder in a directory
for folderName, subfolders, filenames in os.walk('delicious'):
    print('Folder: ' + folderName)
    print('Subfolders: ' + str(subfolders) )
    print('filenames: ' + str(filenames) )

    for subfolder in subfolders:
        print('Directory> ' + subfolder)
    for file in filenames:
        print('File> ' + file)

    print('\n')