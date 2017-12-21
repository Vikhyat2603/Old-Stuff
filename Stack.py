class node:
          def __init__(self,nextnode,val):
                    
                    self.nextnode=nextnode
                    self.val=val

class stack:
          def __init__(self,top,size):
                     
                    self.top=top
                    self.size=size
          
          def push(self,value):
                    
                    n=node(None,value)
                    n.nextnode=self.top
                    self.top=n
                    self.size+=1

          def pop(self):
                    
                    if(self.top==None):return None
                    n=self.top
                    self.top=n.nextnode
                    self.size-=1
                    return n

          def peek(self):
                    if(self.top==None):return None
                    return self.top.val

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string=str(input("Give a string to find it's reverse\n"))
print(string,'\n')

S=stack(None,0)

for i in range(len(string)):
          S.push(string[i])
          print(S.peek())
          
print("\n\n")

for i in range(len(string)):
          print(S.pop().val)
 
