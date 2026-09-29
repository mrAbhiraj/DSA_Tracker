<div align="center">
  <img src="https://takeuforward.org/tufy/tufy-head.svg?dpl=73b33b85-a1c1-42db-9599-b80a7afd9dfc" width="120" alt="takeuforward" />
</div>


# 237. Left Rotate Array by K Places

Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

### Example 1:

**Input**: nums = [1, 2, 3, 4, 5, 6], k = 2

**Output**: nums = [3, 4, 5, 6, 1, 2]

**Explanation**:

rotate 1 step to the left: [2, 3, 4, 5, 6, 1]

rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

### Example 2:

**Input**: nums = [3, 4, 1, 5, 3, -5], k = 8

**Output**: nums = [1, 5, 3, -5, 3, 4]

**Explanation**:

rotate 1 step to the left: [4, 1, 5, 3, -5, 3]

rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]

rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]

rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]

rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]

rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]

rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]

rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]

### Now Your Turn!
Pick the correct output for the given input.

**Input**: nums = [1, 2, 3, 4, 5], k = 4

- [ ] [1, 2, 3, 4, 5]
- [ ] [2, 3, 4, 5, 1]
- [ ] [5, 1, 3, 2, 4]
- [ ] [5, 1, 2, 3, 4]

### Constraints:

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 0 <= k <= 10^5


### Frequently Occurring Doubts

- What if k is greater than or equal to the array length?
- How can this be done in-place?

### Interview Follow-up Questions

- Can this logic be extended to multidimensional arrays?
- What’s the difference between rotation by k and shuffling?
