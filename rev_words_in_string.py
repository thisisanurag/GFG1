t=int(input())
for _ in range(t):
    s=input()
    l=s.split('.')
    for x in range(len(l)):
        if(x==len(l)-1):
            print(l[len(l)-x-1])
        else:
            print(l[len(l)-x-1],end='.')