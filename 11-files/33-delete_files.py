import os, shutil, send2trash

shutil.copy('spam.txt', 'spam2.txt')

# os.unlink() deletes a file
os.unlink('spam2.txt')

if os.path.exists('delicious2'):
    shutil.rmtree('delicious2')
shutil.copytree('delicious', 'delicious2')

try:
    # os.rmdir() removes an empty directory
    os.rmdir('delicious2')
except OSError:
    print('Cannot delete "delicious2"')
# shutil.rmtree() removes a folder and all its content
shutil.rmtree('delicious2')

shutil.copy('spam.txt', 'spam2.txt')

# send2trash.send2trash() sends file to OS recycle bin
send2trash.send2trash('spam2.txt')
