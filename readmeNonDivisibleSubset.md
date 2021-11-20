# ** Not Divisible Subset**
# program:-
## in this program we found maximum subset of list where the sum of 2 numbers in list is not divisible by k which given by user. firstly here i took list by user input 
```
d=[]
    for j in range(k):
        b=[]
        for i in s:
            if i%k==j:
                b.append(i)
        d.append(b)
```
## firstly i took empty list.and run loop range till (k).then i run second loop on our list and then condition check on if the i is% k is equal to j  if this condition is true then i is append in list b and whose reminder is 0  those numbers are append in b and then b  will append in d. as same that all loop will run.we got final list d.
```
y=[]
z=(min(d[0]))
y.append(z)
```
## in that part of this code we took another list . here i used min function for find minimum valu of d[0].beacause the sum 2 values of d[0] is divisible by k so here we took minimum value of this d[0].then it apped on list y.
```
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
count=len(y)
return(count)
        
```
## here i use another one loop  suppose k=7  the loop range start from 1 to(7//2)+1.if k is odd number then check p is not equal to k-p if its true then again check which list has maximum length then append his element in list y .if k is even number we will do previous steps and when p is equal to k-p those d[p] any two element of sum is divisible by k. so here i took minimum value and append it on list y. and after that i use len function to count of subset.at the last we got count of non divisible subset.