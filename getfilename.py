from os import listdir
from os.path import isfile, join
print( [f for f in listdir("M:\\Video") if isfile(join("M:\\Video", f))])

import os
os.path.getsize("M:\\Video\\54ScienceFictionfaitscientifique.avi")

file = open("M:\\Video\\testfile.txt","w")
file.write("Hello World")
file.close()


#files .txt and folder .txt
file = open("testfile.txt", "r") 
for line in file: 
print line

tupName
tupInfo #serie ,movie
tupFolder
tupPath
tupSize
tupExtension
tupNameOK
tupPlaceOK

tupExtDef
tupRemove

#input info or validation
tupNameOK[0] = input("Validate this change:")
import os
>>> for filename in os.listdir("."):
...  if filename.startswith("cheese_"):
...    os.rename(filename, filename[7:])
... https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
