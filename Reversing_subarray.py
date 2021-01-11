arr=[1,2,3,4,5]
print(arr)
k = 3
if k > len(arr):
    print(f"{k} value is not valid")
else:
    for i in range(k // 2):
        arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]
print(arr)
