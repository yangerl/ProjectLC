class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = self.addCurrentNumber(num)
        
        return num
        
    def addCurrentNumber(self, num):
        digitSum = 0
        while num > 0:
            digitSum += num % 10
            num = num / 10
        return digitSum
            
