"""
01. Sort the Array: Sort the array `numbers` in non-decreasing order. This allows us to efficiently calculate distances between pairs of elements.

02. Initialize Distance Bounds: 
   - `minDistance`: Start with 0, representing the smallest possible distance (when two elements are the same).
   - `maxDistance`: Initialize with the difference between the largest and smallest element in the sorted array.

03. Perform Binary Search: 
   - While `minDistance` is less than `maxDistance`, perform the following:
     - Calculate `midDistance` as the middle value between `minDistance` and `maxDistance`.
     - Use the helper function `countPairsWithinDistance` to count the number of pairs with a distance less than or equal to `midDistance`.
     - If the count is less than `k`, move the `minDistance` up to narrow the search range.
     - If the count is greater than or equal to `k`, move the `maxDistance` down.

04. Return the Result: Once the binary search concludes, `minDistance` will be the kth smallest distance, so return it.

Helper Function: `countPairsWithinDistance`
- This function counts the number of pairs within the array that have a distance less than or equal to the given `targetDistance`.
- Use two pointers (`left` and `right`) to efficiently count valid pairs in the sorted array.

Time Complexity: O(n log n + n log D), where n is the length of the array and D is the range of distances. The array is sorted in O(n log n) time, and binary search is performed on the distance with a helper function that runs in O(n) time.
Space Complexity: O(1), as the algorithm uses a constant amount of extra space.
"""

class Solution:
    def smallestDistancePair(self, numbers: List[int], k: int) -> int:
        # 01. Sort the array
        numbers.sort()
        
        # 02. Initialize the distance bounds
        minDistance, maxDistance = 0, numbers[-1] - numbers[0]
        
        # 03. Perform binary search on the distance
        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            # Count pairs with a distance <= midDistance
            if self.countPairsWithinDistance(numbers, midDistance) < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance
        
        # 04. Return the kth smallest distance
        return minDistance

    def countPairsWithinDistance(self, numbers: List[int], targetDistance: int) -> int:
        # Helper function to count valid pairs
        count = 0
        left = 0
        
        # Use two pointers to count pairs
        for right in range(1, len(numbers)):
            while numbers[right] - numbers[left] > targetDistance:
                left += 1
            count += right - left  # Count pairs with valid distances
        
        return count