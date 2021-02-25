class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        
        if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
            return []
        
        # p1, p2, p3
        # v1, v2, v3
        p1 = 0
        p2 = 0
        p3 = 0
        
        v1 = arr1[p1]
        v2 = arr2[p2]
        v3 = arr3[p3] 
        
        solution = []
        maximum = 0
        
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            v1 = arr1[p1]
            v2 = arr2[p2]
            v3 = arr3[p3] 
            if v1 == v2 and v2 == v3:
                solution.append(v1)
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if (v1 < v2 or v1 < v3):
                    p1 += 1
                if (v2 < v1 or v2 < v3):
                    p2 += 1
                if (v3 < v1 or v3 < v2):
                    p3 += 1

        return solution
            
        