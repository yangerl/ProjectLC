
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        # the goal is to find the number of occurences of the Jewel in stirng S
        # let us store how many times each character occurs in S
        # then find the sum for all matches of characters in J that are also in S
        
        stones = {}
        
        for c in S:
            if c not in stones:
                stones[c] = 1
            else:
                stones[c] += 1
                
        numJewels = 0
        for c in J:
            if c in stones:
                numJewels += stones[c]
        
        return numJewels
