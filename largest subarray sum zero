arr = [15,-2,2,-8,1,7,10,23] 

def maxLen(arr):
    my_arr = 0  
    for i in range(len(arr)):           
        arr_sum = 0          
        for j in range(i, len(arr)):           
            arr_sum += arr[j]   
            if arr_sum == 0: 
                my_arr = max(my_arr, j-i+1)   
    return my_arr   
print (" the length of the largest subarray with sum 0 is %d" %  maxLen(arr))
