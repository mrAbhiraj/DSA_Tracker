class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Every n rotations restore the array, so only the remainder matters

        def reverseList(st, en):
            while st < en:
                nums[st], nums[en] = nums[en], nums[st]
                st += 1
                en -= 1

        # Left rotation: reverse each part, then reverse the whole array
        reverseList(0, k - 1)
        reverseList(k, n - 1)
        reverseList(0, n - 1)
        


           
        