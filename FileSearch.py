import os,sys

def makef_d(directory):
          try:
                    fd=os.listdir(directory)
                    for i in range(len(fd)):
                              fd[i]=directory+'/'+fd[i]
                    return fd
          except PermissionError:
                    sys.exit()

def searchfor(file,path):
          fd=makef_d(path)
          direc=[]
          files=[]
          for i in fd:
                    if os.path.isdir(i):
                              direc.append(i)
                    else:
                              files.append(i)
          
          for i in files:
                    if((os.path.basename(i)).lower()==file.lower()):return i
          for i in direc:
                    result=searchfor(file,i)
                    if(result!=None):return result
                    
element=input("What do you want to search for?    ")
maindirectory=os.path.realpath(".")
print("Searching for ",element," in my directory",)
final=os.path.realpath(searchfor(element,maindirectory))                 
if(final==maindirectory):
          print("File Not Found")
else:
          print(final)
          text=(input("Which of these do you want to open?Say 'None' or 'Both' or 'Folder' or 'File' ")).lower()
          if(text=="folder" or text=="both"):
                    index=len(final)-len(element)-1
                    finalpath=os.path.realpath(final[:index])
                    os.startfile(finalpath)
          if(text=="file" or text=="both"):
                    os.startfile(final)


