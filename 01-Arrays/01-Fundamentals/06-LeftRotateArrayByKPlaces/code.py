class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Every n rotations restore the array, so only the remainder matters

        def reverseList(st, en):
            while st <= en:
                temp = nums[st]
                nums[st] = nums[en]
                nums[en] = temp
                st += 1
                en -= 1

        # Three reversals shift the first k elements to the end in-place
        reverseList(0, n-1)
        reverseList(0, k-1)
        reverseList(k, n-1)
        


           
        