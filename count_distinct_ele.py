def countDistinct(arr, n, k):
    z=k
    if (k==0):
        print(0, end=' ')
    else:
        for x in range(n-k+1):
            c=0
            d={}
            for y in range(x,z):
                if(arr[y] not in d):
                    d[arr[y]]=1
                    c+=1
            print(c,end=' ')
            z+=1
    print()
