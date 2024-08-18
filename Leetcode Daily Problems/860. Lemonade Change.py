"""
01. Handle Edge Case: If the first customer does not pay with a $5 bill, return `False` since you can't provide change without starting cash.

02. Initialize Counters: 
   - `five_dollars`: A counter to keep track of the number of $5 bills you have.
   - `ten_dollars`: A counter to keep track of the number of $10 bills you have.

03. Process Each Customer:
   - If the customer pays with a $5 bill, increment the `five_dollars` counter.
   - If the customer pays with a $10 bill, check if you have a $5 bill to give as change:
     - If you have a $5 bill, decrement the `five_dollars` counter and increment the `ten_dollars` counter.
     - If you don't have a $5 bill, return `False`.
   - If the customer pays with a $20 bill, check if you can provide $15 change:
     - Prefer giving one $10 bill and one $5 bill (if available) by decrementing both counters.
     - If you can't do that, check if you have three $5 bills, and if so, decrement the `five_dollars` counter by 3.
     - If neither option is possible, return `False`.

04. Return the Result: If you successfully provide change to all customers, return `True`.

Time Complexity: O(n), where n is the length of the `bills` array. You process each bill exactly once.
Space Complexity: O(1), since only a constant amount of extra space is used for the counters.
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 01. Handle the edge case where the first bill is not $5
        if bills[0] != 5:
            return False
        
        # 02. Initialize counters for $5 and $10 bills
        five_dollars = 0
        ten_dollars = 0
        
        # 03. Process each customer in the queue
        for bill in bills:
            if bill == 5:
                five_dollars += 1  # Increment $5 counter
            elif bill == 10:
                if five_dollars > 0:
                    five_dollars -= 1  # Provide change with one $5 bill
                    ten_dollars += 1  # Increment $10 counter
                else:
                    return False  # Cannot provide change
            else:  # bill == 20
                if five_dollars > 0 and ten_dollars > 0:
                    five_dollars -= 1  # Provide change with one $5 and one $10 bill
                    ten_dollars -= 1
                elif five_dollars >= 3:
                    five_dollars -= 3  # Provide change with three $5 bills
                else:
                    return False  # Cannot provide change
        
        # 04. Return True if all customers received correct change
        return True