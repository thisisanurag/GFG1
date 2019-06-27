import itertools
d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=[int(x) for x in s.split()]
    s=[]
    for x in l:
        k=list(d[x])
        s.append(k)
    ans=list(itertools.product(*s))
    for x in ans:
        print("".join(x),end=' ')
    print()
