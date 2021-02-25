class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        # left = 0
        # r = 0
        # solution = 0/[]/{}
        # 
        # loop to keep track of our window
        # while right is within bounds:
        #   do something with current_value
        #   do something with current_index
        #   if condition, to check validity of window:
        #       update solution
        #       update pointer
        #   slide right pointer by 1
        # maybe check window again?
        # return
        
        # BFS/DFS
        # queue or stack
        # adding our starting point into the DS
        # while DS is not empty:
        #   curr_node = DS.pop()
        #   adding neighbors
        #   if statement to check on what im searching:
        #       update solution
        # returning
        
        left = 0
        right = 0
        solution = 0
        letters = {}
        while right < len(s):
            current_char = s[right]
            letters[current_char] = right
            
            if len(letters.keys()) > 2:
                # we need to find the least recently used character
                solution = max(solution, right - left)
                lru_char = self.lru(letters)
                lru_char_index = letters[lru_char]
                left = lru_char_index + 1
                letters.pop(lru_char)
                
            right += 1
        solution = max(solution, right-left)
        return solution
    
    def lru(self, letters_map):
        # this returns the character that was least recently used
        lru_index = None
        character_to_return = ""
        
        for key in letters_map.keys():
            current_keys_index = letters_map[key]
            if lru_index is None:
                lru_index = current_keys_index
                character_to_return = key 
            else:
                if lru_index > current_keys_index:
                    lru_index = current_keys_index
                    character_to_return = key 
                    
        return character_to_return
                
                    
        