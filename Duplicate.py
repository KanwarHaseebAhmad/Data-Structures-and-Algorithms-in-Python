def duplicate(arr,n):
    ans = []
    arr = sorted(arr)
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            ans.append(arr[i])
    
    if ans:
        sorted(list(set(ans)))
    else:
        return -1
    return ans
print(duplicate([0,2,4,8,6,0,8],7))
