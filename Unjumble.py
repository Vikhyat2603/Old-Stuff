#45333 words
import str_ops
text=open("EnglishWords.txt","r")
words=[]
for line in text:
          words.append((line.lower().strip()))
while(1):
          user=(input("Enter jumbled form of existing word.   ")).strip().lower()
                                                 
          def isjumbled(str1,str2):
                    if (len(str1)==len(str2)):
                              temp1=str1
                              temp2=str2
                              while(temp1[0]!=None):
                                        letter=temp1[0]
                                        index=str_ops.containsindex(temp2,letter)
                                        if index==None:return False
                                        temp1=str_ops.delete(temp1,0)
                                        temp2=str_ops.delete(temp2,index)
                                        try:
                                                  temp1[0]
                                        except IndexError:
                                                  break
                              return True
                    return False

          for word in words:
                    if(isjumbled(word,user)):
                              print(word)


