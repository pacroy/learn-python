import os

totalSize = 0
for filename in os.listdir(os.getcwd()):
    abspath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(abspath):
        print(abspath + ' = <directory>' )
        continue
    filesize = os.path.getsize(abspath)
    print(abspath + ' = ' + str(filesize))
    totalSize += filesize

print("Total = " + str(totalSize))
