# shutil = shell utility
import shutil, os
# shutil.copy() copies a file
shutil.copy('spam.txt', 'spam2.txt')

# shutil.copytree() copies a folder and all files/subfolders within
# shutil.rmtree() remove a folder and all files/subnfolders within
if os.path.exists('delicious2'):
    shutil.rmtree('delicious2')
shutil.copytree('delicious', 'delicious2')

# shutil.move() moves a file or folder, can be used to rename
shutil.move('spam2.txt', 'spam2.bak')

# Clean up
os.remove('spam2.bak')
shutil.rmtree('delicious2')
