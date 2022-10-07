def findIndex(a,N,key):
    d = []
    for i in range(N):
        if a[i]==key:
            d.append(i)
        
    if len(d) != 0:
        return d[0],d[-1]
    else:
        return -1, -1

arr= [4,2,5,3,5,2,8,2,0]
n = 9
k = 5
print(findIndex(arr,n,k))
