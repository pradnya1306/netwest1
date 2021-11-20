

def nonDivisileSubset(k,s):
    d=[]
    for j in range(k):
        b=[]
        for i in s:
            if i%k==j:
                b.append(i)
        d.append(b)
    # print(d)
    y=[]
    z=(min(d[0]))
    y.append(z)
    for p in range(1,(k//2)+1):
        if p!=k-p:
            if len(d[p])>len(d[k-p]):
                for h in range(len(d[p])):
                    y.append(d[p][h])
            else:
                for x in range(len(d[k-p])):
                    y.append(d[k-p][x])
        else:
            a=min(d[p])
            y.append(a)
    # print(y)
    count=len(y)
    return(count)

size=int(input("enter the length of list : "))
k=int(input("enter the number which is not divisible of sum : "))
s=[]
for i in range (size):
    m=int(input("enter the number :"))
    s.append(m)

print(nonDivisileSubset(k,s))
