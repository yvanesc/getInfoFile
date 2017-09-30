import os
files = os.listdir('/media/pi/')
for f in files:
    print(f)#attach on sub listed
    for dirname, dirnames, filenames in os.walk('/media/pi/'+ f):
        for subdirname in dirnames:
            print(subdirname)
        for filename in filenames:
            print(filename)
