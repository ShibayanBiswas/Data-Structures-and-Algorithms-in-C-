"""
01. Handle Edge Case for n = "1":
   - If the input `n` is "1", return "0" as the closest palindrome.

02. Generate Basic Palindrome Candidates:
   - Consider the smallest palindrome larger than `n` by adding 1 to the first half and mirroring it.
   - Consider the largest palindrome smaller than `n` by subtracting 1 from the first half and mirroring it.
   - Consider direct mirroring of the first half to create a potential palindrome.

03. Construct Palindrome Candidates:
   - Extract the first half of the string `n` and convert it to an integer (`prefix_number`).
   - Generate three candidates by adjusting the prefix (subtract 1, keep the same, add 1) and mirroring it.
   - If `n` has an even number of digits, mirror the entire prefix.
   - If `n` has an odd number of digits, mirror only the first half of the prefix.

04. Handle Edge Cases for Larger and Smaller Palindromes:
   - Add the smallest palindrome with one less digit (e.g., "999...999").
   - Add the smallest palindrome with one more digit (e.g., "1000...0001").

05. Remove the Original Number:
   - Remove the original number `n` from the set of candidates.

06. Find the Closest Palindrome:
   - Compare all candidates and find the one with the smallest absolute difference from `n`.
   - If there is a tie, return the smaller palindrome.

Time Complexity: O(1), since the maximum length of `n` is 18 digits, making the operations constant time.
Space Complexity: O(1), as the space used for storing candidates is fixed and independent of input size.
"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()
        
        # 01. Handle edge case for n = "1"
        if n == "1":
            return "0"
        
        # 02. Create the basic middle palindrome by mirroring the first half
        prefix = n[:(length + 1) // 2]
        prefix_number = int(prefix)
        
        # 03. Generate the candidates by adjusting the prefix
        for i in [-1, 0, 1]:
            new_prefix = str(prefix_number + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)
        
        # 04. Handle edge cases for larger and smaller palindromes
        candidates.add(str(10**(length-1) - 1))  # Smallest palindrome with one less digit
        candidates.add(str(10**length + 1))  # Smallest palindrome with one more digit
        
        # 05. Remove the original number from the candidates set
        candidates.discard(n)
        
        # 06. Find the closest palindrome
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome