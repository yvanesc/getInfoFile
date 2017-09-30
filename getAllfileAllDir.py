import os
import string
import datetime

filePath = "M:\\pathInfo.txt"
fileName = "M:\\fileInfo.txt"
fileInfo = "M:\\extInfo.txt"
today = datetime.date.today()
path = "M:\\Video\\Movies\\" #sys.path[0]

fileP = open(filePath,"w")
fileN = open(fileName,"w")
fileI = open(fileInfo,"w")
diff =[]
i=0
#fileN.write(str(today + "\n"))
print(today)
for dirname, dirnames, filenames in os.walk(path):
    for subdirname in dirnames:
        #print("DIRECTORY: ", os.path.join(dirname, subdirname))
        fileP.write(os.path.join(dirname, subdirname) + "\n")
    for filename in filenames:
        sourceOri = os.path.join(dirname, filename)
        source = os.path.join(dirname, filename) + "***"
        posString=sourceOri.index('.')
        posFrEnd=len(sourceOri)-posString
        if posFrEnd  > 4:
            #print (sourceOri)
            #print(posFrEnd)
            gargul="test"
            #remove dot
        else:
            #print(sourceOri[posString+1:])
            seen =set(diff)
            itemSrc = sourceOri[posString+1:]
            if itemSrc not in seen:
                seen.add(itemSrc)
                diff.append(itemSrc)
                #print(itemSrc)
                
                if os.path.getsize(sourceOri) > 104857600:#more big then 100M
                    print(itemSrc)
                    fileI.write(itemSrc +"> 100M \n")
                else:
                    fileI.write(itemSrc +"\n")
            #diff[i] = sourceOri[posString+1:]
            #if len(diff) > 1:
                #for tmpTest in diff:
                    
        #print(source + "***")
        #print(str(os.path.getsize(sourceOri)))
        #source = str(source, encoding='utf-8', errors = 'ignore')
        if os.path.getsize(sourceOri) > 1073741824:
            srcInf = str(os.path.getsize(sourceOri) // 1073741824)
            srcInf =srcInf+"."+str(os.path.getsize(sourceOri) // 1048576)+"G"
        elif os.path.getsize(sourceOri) > 1048576:
            srcInf = str(os.path.getsize(sourceOri) // 1048576)+"M"
        elif os.path.getsize(sourceOri) > 1024:
            srcInf = str(os.path.getsize(sourceOri) // 1024)+"K"            
        else:
            srcInf = str(os.path.getsize(sourceOri))
        source = source  + srcInf
        fileN.write(source + "\n")
fileP.close()
fileN.close()
fileI.close()
