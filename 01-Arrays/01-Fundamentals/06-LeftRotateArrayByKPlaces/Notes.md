# Notes

- Pattern: Array reversal
- Time Complexity: O(n)
- Space Complexity: O(1)
- This problem asks for a left rotation: move the first `k` elements to the end.
- Fast recognition: Left = reverse first part -> reverse second part -> reverse whole array.

## Why use `k % n`?

- `n` is the number of elements; `k` is the number of requested rotations.
- Every `n` rotations bring the array back to its original order, so only the remainder changes it.

Example: `n = 6`, `k = 8` means `8 % 6 = 2`. Rotating 8 times has the same result as rotating 2 times.

## Left rotation with `k = 2`

Start: `[1, 2, 3, 4, 5, 6]`

Goal: `[3, 4, 5, 6, 1, 2]`

1. Reverse the first `k` elements: `[2, 1, 3, 4, 5, 6]`
2. Reverse the remaining elements: `[2, 1, 6, 5, 4, 3]`
3. Reverse the whole array: `[3, 4, 5, 6, 1, 2]`

Code call order:

```python
reverseList(0, k - 1)  # reverse first k elements
reverseList(k, n - 1)  # reverse remaining elements
reverseList(0, n - 1)  # reverse the whole array
```

## Right rotation pattern

Right rotation moves the last `k` elements to the beginning.

Start: `[1, 2, 3, 4, 5, 6]`, `k = 2`

1. Reverse the whole array: `[6, 5, 4, 3, 2, 1]`
2. Reverse the first `k` elements: `[5, 6, 4, 3, 2, 1]`
3. Reverse the remaining elements: `[5, 6, 1, 2, 3, 4]`

Fast recognition: Right = reverse whole array -> reverse first `k` -> reverse the rest.
