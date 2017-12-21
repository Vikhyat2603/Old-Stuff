import os,sys
thisfile= (os.path.basename(sys.argv[0]))
workdir="./Sub"
files=os.listdir(workdir)
for i in range(len(files)):
          if(files[i]!=thisfile and files[i].endswith(".srt")):
                    os.rename(workdir   +  "/"  +   files[i]  ,   workdir  +  "/"  +  ( "Episode"+" "+str(i+1)+".srt")   )
