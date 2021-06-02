# Function to check if x is power of 2  
def check(x): 
      
    # Returns true if x is a power of 2  
    return x and (not(x & (x - 1))) 
  
def count(arr, n):  
      
    cnt = 0
  
    # Iterate for all possible pairs  
    for i in range(n - 1): 
        for j in range(i + 1, n):  
  
            # Bitwise and value of  
            # the pair is passed  
            if check(arr[i] & arr[j]):  
                cnt = cnt + 1
  
    # Return the final count  
    return cnt  
  
# Given array  
arr = [0,2,4] 
n = len(arr) 
  
# Function Call  
print(count(arr, n)) 
  
