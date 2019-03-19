import os, re

atRegex = re.compile(r'.zip')

for folderName, subfolders, filenames, in os.walk(): #<- Directory that you want to search goes here
    for subfolder in subfolders:
        if atRegex.search(subfolder):
            print ('SUBFOLDER OF ' + folderName + ' : ' + subfolder + '!!!Zip File Found!!!')

    for filename in filenames:
        if atRegex.search(filename):
            print ('FILE INSIDE ' + folderName + ' : ' + filename + '!!!Zip File Found!!!')