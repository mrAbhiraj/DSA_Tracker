class Solution:
    def rotateArrayByOne(self, nums):

        fst_elem = nums[0]
        for i in range(0 , len(nums)-1 , 1):
            nums[i] = nums[i+1]
        
        nums[len(nums)-1] = fst_elem