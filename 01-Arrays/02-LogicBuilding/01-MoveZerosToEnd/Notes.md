# Notes

- Pattern: Partitioning / two-pointer
- Time Complexity: O(n)
- Space Complexity: O(1)
- Recall: `i` scans; `j` marks where the next non-zero belongs.

## How the pointers work

- `i` visits every index from left to right.
- `j` is the next position where a non-zero value should be placed.
- When `nums[i]` is non-zero, swap `nums[i]` with `nums[j]`, then increment `j`.
- When `nums[i]` is zero, do nothing. Keep scanning until a non-zero can be moved into its place.
- At the start of each iteration, indexes before `j` contain the non-zero values found so far, in their original order.
- The scan goes left to right, so the relative order of non-zero values stays unchanged. The array is modified in-place; the method does not return a new array.

## Dry run

Input: `[0, 1, 0, 3, 12]`

| `i` | `nums[i]` | Action | Array after action | `j` after action |
|-----|-----------|--------|--------------------|------------------|
| 0 | 0 | Zero, skip | `[0, 1, 0, 3, 12]` | 0 |
| 1 | 1 | Swap indexes 0 and 1 | `[1, 0, 0, 3, 12]` | 1 |
| 2 | 0 | Zero, skip | `[1, 0, 0, 3, 12]` | 1 |
| 3 | 3 | Swap indexes 1 and 3 | `[1, 3, 0, 0, 12]` | 2 |
| 4 | 12 | Swap indexes 2 and 4 | `[1, 3, 12, 0, 0]` | 3 |

Result: `[1, 3, 12, 0, 0]`

## Edge cases

- **No zeros**, for example `[2, 1, 3]`: every non-zero swaps with itself; the array stays unchanged.
- **All zeros**, for example `[0, 0, 0]`: every value is skipped; the array stays unchanged.
- **Zeros at the beginning**, for example `[0, 0, 4]`: `j` stays at 0 until `4` is found, then `4` moves to the front.
- **Zeros between non-zeros**, for example `[1, 0, 2]`: `2` moves into the next non-zero position; the order `1, 2` is preserved.
- **Zeros at the end**, for example `[1, 2, 0, 0]`: non-zeros remain in place and zeros are already at the end.
- **Negative values** are non-zero too, so they are kept in their original order, for example `[-2, 0, 5]` becomes `[-2, 5, 0]`.
- **Single element**: `[0]` and `[7]` both remain unchanged.
- **Empty array**: the loop runs zero times and the method makes no changes. The stated problem constraints require at least one element, but the loop still handles this case.

## Complexity

- Time: `O(n)` because each element is checked once.
- Extra space: `O(1)` because swaps are done inside the input array.
