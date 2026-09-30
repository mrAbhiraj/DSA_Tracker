class Solution:
    def findMaxConsecutiveOnes(self, nums):

        cnt = 0
        temp_cnt = 0
    
        for elem in nums:
            if elem == 1:
                temp_cnt += 1
                if cnt < temp_cnt:
                    cnt = temp_cnt
            else:
                temp_cnt = 0
            
        return cnt 

        