def append(string,element):
    return string+element
def delete(string,index):
    ct=0
    stringcopy=""
    if index=="last":
        while(ct<len(string)-1):
            stringcopy=stringcopy+string[ct]
            ct+=1   
    elif(index!="all"):
        while(ct<index):
            stringcopy=stringcopy+string[ct]
            ct+=1
        ct+=1    
        while(ct<len(string)):
            stringcopy=stringcopy+string[ct]
            ct+=1
    return stringcopy
def add(string,element,index):
    ct=0
    stringcopy=""
    while(ct<index):
        stringcopy=stringcopy+string[ct]
        ct+=1
    stringcopy=stringcopy+element
    while(ct<len(string)):
        stringcopy=stringcopy+string[ct]
        ct+=1
    return stringcopy
def containsindex(string,element):
    ct=0
    while(ct<len(string)):
        if(string[ct]==element):
            return ct
        ct+=1
    return None   
def substring(string,start,end):
    ct=start
    stringcopy=""
    while(ct<=end):
        stringcopy+=string[ct]
        ct+=1
    return stringcopy

