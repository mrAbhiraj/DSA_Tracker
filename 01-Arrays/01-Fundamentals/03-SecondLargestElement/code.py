class Solution:
    def secondLargestElement(self, nums):
        # Track the largest value seen so far
        first_mx = nums[0]

        # Track the second largest value seen so far
        sec_mx = -1

        for elem in nums:
            if elem > first_mx:
                sec_mx = first_mx
                first_mx = elem
            elif first_mx > elem and elem > sec_mx:
                sec_mx = elem

        return sec_mx

        