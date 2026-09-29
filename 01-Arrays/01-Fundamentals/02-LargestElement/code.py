class Solution:
    def largestElement(self, nums):
        # Start with the first element as the current maximum
        mx_value = nums[0]

        # Traverse the array and update the maximum whenever needed
        for elem in nums:
            if mx_value < elem:
                mx_value = elem

        return mx_value
