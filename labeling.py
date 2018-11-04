from os import listdir
from os.path import isfile, join
import os
from shutil import copyfile

dirSet = ['card','human','paper']
sourcePath = 'C:/P_workspace/workspace/개발과제/images/'
destPath = 'C:/P_workspace/workspace/개발과제/train/'
newDirName = 0
for targetDir in dirSet:
    #onlyFiles = [(f for f in listdir(sourcePath+targetDir) if isfile(join(sourcePath+targetDir),f))]

    newName = 0
    newTargetDir = destPath+'n'+str(newDirName)
    os.mkdir(newTargetDir)
    files=os.listdir(sourcePath+targetDir)
    for name in range(0,len(files)):
        print ('copy '+sourcePath+targetDir+'/'+str(name))
        copyfile(sourcePath+targetDir+'/'+targetDir+str(newName)+'.jpg',newTargetDir+'/'+str(newDirName)+'_'+str(newName)+'.jpg')
        newName+=1
    newDirName+=1

