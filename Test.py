text=open("EnglishWords.txt","r")
words=[]
for line in text:
          words.append((line.lower().strip()))
length=0
for word in words:
          if len(word)>length:
                    length=len(word)
                    lowo=word
print(lowo)
