class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # Which kid has the maximum
        # condition: current kid + extra >= maximum
        # trying for O(N) to find the maximum
        # modified 2 sum: where you dont know what your target is
        solution = []
        maximum = 0
        
        for candy in candies:
            if candy > maximum:
                maximum = candy
        
        for candy in candies:
            solution.append(candy + extraCandies >= maximum)
            
        return solution