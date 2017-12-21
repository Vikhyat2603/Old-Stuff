def run():
    import str_ops,math
    global ans
    ct=0
    op=''
    data=""
    numbers="0123456789."
    ########################################################################################
    def get_nums():
        global a,b,op,numa,numb
        a=""
        b=""
        ct=0
        if(data[0]=='-'):
            a="-"
            ct=1
        while(str_ops.contains(numbers,data[ct])):
            a=a+data[ct]
            ct+=1
            if ct==len(data):
                break
        op=data[ct]
        ct+=1
        if(data[ct]=='-'):
            b="-"
            ct+=1
        while(str_ops.contains(numbers,data[ct])):
            b=b+data[ct]
            ct+=1
            if ct==len(data):
                break
        numa=0
        numb=0
        numa=float(a)
        numb=float(b)
        print("A:",numa,',',"B:",numb)
    ########################################################################################
    def calculate():
        global numa,numb,ans,op
        if op=='+':
            ans=numa+numb
        elif op=='-':
            ans=numa-numb
        elif op=='*':
            ans=numa*numb
        elif op=='/':
            ans=numa/numb
        elif op=='^':
            ans=numa**numb
        print(" ",numa,op,numb,'=',ans)
    ########################################################################################
    data=input("Give input\n")
    while (str_ops.contains(data,'+')|str_ops.contains(data,'-')|str_ops.contains(data,'*')|str_ops.contains(data,'/')|str_ops.contains(data,'^')):
        print(data)
        get_nums()
        calculate()
        ct=0
        stringans=str(ans)
        while ct<=(len(a)+len(b)):
            data=str_ops.delete(data,0)
            ct+=1
        data=str_ops.add(data,stringans,0)
    ########################################################################################
    print("\nFinal answer is:",data,"\n")
    command=input("Do you wish to restart?(Y/N)\n")
    if (command=='Y')|(command=='y'):
        run()
run()
