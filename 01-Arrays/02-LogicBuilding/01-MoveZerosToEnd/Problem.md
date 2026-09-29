<div align="center">
  <img src="https://takeuforward.org/tufy/tufy-head.svg?dpl=73b33b85-a1c1-42db-9599-b80a7afd9dfc" width="120" alt="takeuforward" />
</div>

# Move Zeros to End

Given an array `nums`, move all `0` values to the end of the array while keeping the relative order of all non-zero elements the same.

### Example 1:

**Input**: nums = [0, 1, 0, 3, 12]

**Output**: [1, 3, 12, 0, 0]

### Example 2:

**Input**: nums = [0, 0, 1]

**Output**: [1, 0, 0]

### Constraints:

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9


### Frequently Occurring Doubts

- What if the array already has no zeros?
- How do we preserve the relative order of non-zero elements?

### Interview Follow-up Questions

- Can this be solved using a two-pointer approach?
- Can we do it in-place without extra space?
