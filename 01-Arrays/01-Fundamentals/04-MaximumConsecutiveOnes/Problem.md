<div align="center">
  <img src="https://takeuforward.org/tufy/tufy-head.svg?dpl=73b33b85-a1c1-42db-9599-b80a7afd9dfc" width="120" alt="takeuforward" />
</div>


# 213. Maximum Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1s in the array.

A binary array is an array that contains only 0s and 1s.

### Example 1:

**Input**: nums = [1, 1, 0, 0, 1, 1, 1, 0]

**Output**: 3

**Explanation**: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s.

### Example 2:

**Input**: nums = [0, 0, 0, 0, 0, 0, 0, 0]

**Output**: 0

**Explanation**: No 1s are present in nums, thus we return 0.

### Now Your Turn!
Pick the correct output for the given input.

**Input**: nums = [1, 0, 1, 1, 1, 0, 1, 1, 1]

- [ ] 1
- [ ] 3
- [ ] 4
- [ ] 7

### Constraints:

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.


### Frequently Occurring Doubts

- What is the time complexity, and can it be optimized further?
- How does the algorithm handle arrays with alternating 1s and 0s?

### Interview Follow-up Questions

- How would you modify the algorithm to return the indices of the maximum segment of consecutive 1s?
- How would you handle a streaming input (data arriving one bit at a time)?
