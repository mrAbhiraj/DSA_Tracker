# Notes

- Pattern: Array reversal
- Time Complexity: O(n)
- Space Complexity: O(1)
- Recall: Move the first k elements to the end
- Fast recognition: Reverse all -> reverse first k -> reverse the rest

## Why use `k % n`?

- `n` is the number of elements in the array; `k` is how many positions to rotate.
- After `n` rotations, the array returns to its original order. Full groups of `n` rotations do not change the final result.
- So `k % n` keeps only the rotations that still have an effect.

Example with 5 elements:

| Given k | Calculation | Effective rotations |
|---------|-------------|---------------------|
| 7 | 7 % 5 | 2 |
| 10 | 10 % 5 | 0 |

For `k = 7`, think of 5 rotations returning the array to its start, then 2 more rotations. Only those 2 extra rotations matter.

## Three reversals for a left rotation

For `[1, 2, 3, 4, 5]` with `k = 2`, the goal is `[3, 4, 5, 1, 2]`:

1. Reverse the first `k` elements: `[2, 1, 3, 4, 5]`
2. Reverse the remaining elements: `[2, 1, 5, 4, 3]`
3. Reverse the whole array: `[3, 4, 5, 1, 2]`

Important: the current reversal call order in `code.py` reverses the whole array first, so it performs a **right rotation**. For this problem's left rotation, use the three steps above.
