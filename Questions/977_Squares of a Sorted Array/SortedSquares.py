class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
    
    def sortedSquares3(self, nums):
        sol = []
        for num in nums:
            sol.append(num * num)
        return sorted(sol)
    
    def sortedSquares2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        starter_index = self.starter_index(nums)
        left = starter_index - 1
        right = starter_index + 1
        solution = [nums[starter_index] * nums[starter_index]]
        
        while left >= 0 or right < len(nums):
            if left < 0:
                # process right
                right_num = nums[right] 
                square = right_num * right_num
                solution.append(square)
                right += 1
            elif right >= len(nums):
                # process left side
                left_num = nums[left]
                square = left_num * left_num
                solution.append(square)
                left -= 1
            else:
                # do the comparison thing
                right_num = nums[right] 
                left_num = nums[left]
                l_square = left_num * left_num
                r_square = right_num * right_num
                if l_square < r_square:
                    solution.append(l_square)
                    left -= 1
                else:
                    solution.append(r_square)
                    right += 1
                    
        return solution
    
     def starter_index(self, nums):
        # return where it first becomes non-negative
        # but also checking which is smaller compared to previous value
        for i, num in enumerate(nums):
            if num >= 0:
                prevIndex = i - 1
                if prevIndex < 0:
                    return i 
                prevNum = nums[prevIndex]
                if prevNum * prevNum < num * num:
                    return prevIndex
                else:
                    return i
        return len(nums) - 1
    
        