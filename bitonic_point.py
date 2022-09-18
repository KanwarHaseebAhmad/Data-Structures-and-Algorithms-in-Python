def bitonicPoint(a,n):
    maximum = a[0]
    for i in range(n):
        if a[i]>maximum:
            maximum=a[i]
    return maximum

print(bitonicPoint([1,2,3,4,5,6,7,8,9],9))
