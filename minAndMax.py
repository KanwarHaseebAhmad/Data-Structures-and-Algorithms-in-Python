def minAndMax(a,n):
    maximum=a[0]
    minimum=a[0]
    for i in range(n):
        if a[i]>maximum:
            maximum=a[i]
        elif a[i]<minimum:
            minimum=a[i]
    return minimum, maximum

arr=[0,2,0,5,0,4]
Num=6
print(minAndMax(arr,Num))
