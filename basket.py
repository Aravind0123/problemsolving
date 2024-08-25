def score(ops):
    new_ops=[]
    for i,x in enumerate(ops):
        if x.isdigit():
            new_ops.append(int(x))
        elif x == "-2":
            new_ops.append(int(-x))
        elif x=="+" :
            if len(new_ops)>=2:
                new_ops.append(new_ops[-1]+new_ops[-2])
        elif x=="D" :
            if len(new_ops)>=1:
                new_ops.append(new_ops[-1]*2)
        elif(x=="C"):
            if len(new_ops)>=1:
                new_ops.pop()
    print(sum(new_ops))
ops=["5","2","C","D","+"]
score(ops)