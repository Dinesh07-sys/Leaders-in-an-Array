# Leaders in an Array

A Python program that finds all leader elements in an array by scanning from right to left and keeping track of the maximum value seen so far.

## What Is a Leader?

An element is considered a leader if it is greater than or equal to every element appearing to its right.

The rightmost element is always a leader because there are no elements after it.

For example:

```text
Array:    10  22  12  3  0  6
Leaders:  22  12  6
```

The program identifies these elements by processing the array from the right side.

## How It Works

The method first handles an empty array:

```python id="m6t7sq"
if n == 0:
    return []
```

It then creates a list for storing the leaders and initializes the rightmost element as the current maximum:

```python id="o8j2qk"
leaders = []
max_right = nums[n - 1]
```

Since the last element is automatically a leader, it is added immediately:

```python id="h0m2vw"
leaders.append(nums[n - 1])
```

The remaining elements are examined from right to left:

```python id="8x9z3n"
for index in range(n - 2, -1, -1):
```

For every element, the program checks whether it is greater than or equal to the maximum value found on its right:

```python id="e4a7ph"
if nums[index] >= max_right:
    leaders.append(nums[index])
```

The right-side maximum is then updated:

```python id="r1d6nk"
max_right = max(max_right, nums[index])
```

These steps allow the program to determine whether each element qualifies as a leader without repeatedly scanning the elements to its right.

## Why Traverse From Right to Left?

The definition of a leader depends entirely on the elements to its right.

By starting at the end of the array, the program already knows the maximum value among the elements processed so far. This makes each new comparison immediate.

For example:

```text
10  22  12  3  0  6
                    ↑
                 Start here
```

Moving backward:

```text
10  22  12  3  0  6
                ↑
```

The current element only needs to be compared with the maximum encountered on its right.

## Result Ordering

Because the array is scanned from right to left, leaders are initially stored in reverse order.

The program therefore calls:

```python id="k5y2px"
leaders.reverse()
```

before returning the result, restoring the original left-to-right ordering.

## Example

The program uses:

```python id="q5n7fx"
nums = [10, 22, 12, 3, 0, 6]
```

The leaders are:

```text
22 12 6
```

The example is executed through `leaders_in_array()` and printed from the main section.

## Algorithm

1. Return an empty list if the array is empty.
2. Start with the last element as the current right-side maximum.
3. Add the last element to the leaders list.
4. Traverse the remaining elements from right to left.
5. Add an element if it is greater than or equal to the current maximum.
6. Update the maximum.
7. Reverse the leaders list.
8. Return the result.

## Complexity

| Metric          | Complexity |
| --------------- | ---------- |
| Time            | O(N)       |
| Auxiliary Space | O(N)       |

The array is traversed once. The `leaders` list stores the elements identified as leaders.

## Key Concepts

* Array traversal
* Right-to-left scanning
* Running maximum
* Leader element identification
* List reversal
* Linear-time processing

## Running the Program

Run:

```bash id="c2r8mv"
python "Leaders in an Array.py"
```

Expected output:

```text id="a9x2kp"
22 12 6
```
