import random as rn
n=int(input("Enter no of elements: "))
ar = rn.sample(range(1,10),n)
print("input array: ",ar)
k =int(input("Enter no of elements to be reversed: "))
print("\n")
#reverse(ar, n, k) 
op=[]
i=0
if k> len(ar):
    print("Please enter the number ie less than length of the array")
    
else:
    while(i<n):
        a =i
        b=min(i + k - 1, n - 1)
        while (a < b):
            ar[a], ar[b] = ar[b], ar[a] 
            a+= 1; 
            b-=1
        i+= k
    for j in range(0, n): 
        op.append(ar[j])
    print("output array: ",op)
