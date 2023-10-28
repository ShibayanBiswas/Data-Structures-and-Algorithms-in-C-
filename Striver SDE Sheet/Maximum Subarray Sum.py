'''

Let us check for all possible subarrays of the array. For this, we run two loops, where the outer loop points to the left boundary 
and the inner loop points to the outer boundary of the subarray. Using another loop inside, find the sum of this subarray. Compare 
it with the maximum subarray sum obtained so far. After checking all the subarrays, simply return the maximum sum found.

Time Complexity : O(n ^ 3), where ‘n’ is the length of the array. There are n * (n + 1) / 2 subarrays in total, and for each subarray,
we find its sum in O(n) time.

Space Complexity : O(1), as constant extra space is required.

'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    ans = 0
    for i in range(n) :
        for j in range(i, n) :
            tempSum = 0
            for k in range(i, j + 1) :
                tempSum += arr[k]
            ans = max(ans, tempSum)
    return ans
    

#taking inpit using fast I/O
def takeInput() :
    n =  int(input())
    if(n == 0) :
        return list(), n
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))