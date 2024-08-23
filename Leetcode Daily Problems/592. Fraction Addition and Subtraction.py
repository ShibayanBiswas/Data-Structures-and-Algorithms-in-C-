"""
01. Parse the Expression:
   - Use regular expressions to extract all the integers from the input string `expression`. These integers represent the numerators and denominators of the fractions in the expression.

02. Initialize the Result:
   - `numerator`: Initialize the numerator of the result to 0.
   - `denominator`: Initialize the denominator of the result to 1.

03. Perform Fraction Addition/Subtraction:
   - Iterate through the list of extracted numbers in pairs (numerator and denominator).
   - For each fraction, update the current `numerator` and `denominator` of the result using the formula:
     - `numerator = numerator * current_denominator + current_numerator * denominator`
     - `denominator = denominator * current_denominator`
   - This formula accounts for the addition or subtraction of fractions with different denominators.

04. Simplify the Result:
   - Find the greatest common divisor (gcd) of the `numerator` and `denominator`.
   - Divide both `numerator` and `denominator` by the gcd to simplify the fraction.

05. Return the Result:
   - Return the simplified fraction in the format `numerator/denominator`.

Time Complexity: O(n), where n is the length of the expression. Parsing the expression and calculating the gcd take linear time.
Space Complexity: O(1), since the solution uses a constant amount of extra space.
"""

import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 01. Parse the expression to extract all integers
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        
        # 02. Initialize the result's numerator and denominator
        numerator = 0
        denominator = 1
        
        # 03. Perform fraction addition/subtraction
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den
        
        # 04. Simplify the result using the greatest common divisor (gcd)
        common_divisor = gcd(numerator, denominator)
        
        # 05. Return the result in the format "numerator/denominator"
        return f"{numerator // common_divisor}/{denominator // common_divisor}"