'''


We will check all the possible ways of buying and selling stocks. We will fix the time we are buying the stock and check all the 
possible minutes we can sell this stock and update the maximum profit we can get. Now we will take the maximum profit for all the 
possible buying time and that would be our final maximum profit.

Time Complexity : O(N^2), where ‘N’ is the size of the array. Since we are iterating over all the possible buying time and for each 
we are considering all the selling time, the final time complexity will be O(N^2).

Space Complexity : O(1). Constant space is used.

'''

def maximumProfit(prices):
    
    # Variable to store the maximum profit.
    maxProfit = 0
    n = len(prices)
    
    # Iterating over the array for the buying price.
    for i in range(n - 1):
        
        '''
                Variables to store current buying price and
                maximum profit for if we buy stock at this minute.
        '''
        buy = prices[i]
        curMaxProfit = 0
        
        '''
                Iterating over the next minutes for selling price,
                and storing the maximum profit we can get in curMaxProfit.
        '''
        for j in range(i + 1, n):
            curMaxProfit = max(curMaxProfit, (prices[j] - buy))
            
        '''
                Taking the maximum of all the curMaxProfit and
                storing it in the maxProfit variable.
        '''
        maxProfit = max(maxProfit, curMaxProfit)
        
    return maxProfit
