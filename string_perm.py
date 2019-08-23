from itertools import permutations
t=int(input())
for _ in range(t):
    s=str(input())
    perm=permutations(s)
    l=list(perm)
    l.sort()
    for i in l:
        print(''.join(i),end=' ')
    print()
