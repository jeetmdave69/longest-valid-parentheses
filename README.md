# Longest Valid Parentheses

A Python solution for finding the length of the longest valid parentheses substring.

## Examples

- Input: `(()`  
  Output: `2`

- Input: `)()())`  
  Output: `4`

- Input: empty string  
  Output: `0`

## Approach

The program uses a stack to store indexes.

- `-1` is added first as a starting boundary.
- The index of every opening bracket is pushed onto the stack.
- For a closing bracket, the top index is removed.
- If the stack becomes empty, the current index becomes the new boundary.
- Otherwise, the current valid length is calculated using the current index and the top of the stack.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Run

```bash
python solution.py
```

Then enter a string containing only `(` and `)`.