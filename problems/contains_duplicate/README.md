# Contains Duplicate

## Problem
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Examples
- `[1,2,3,1]` -> `true`
- `[1,2,3,4]` -> `false`
- `[1,1,1,3,3,4,3,2,4,2]` -> `true`

## Approach
Use a set/hash set to track values seen so far.
- If a value is already in the set, return `true`
- Otherwise add it and continue
- If the loop finishes, return `false`

## Time complexity
- `O(n)`

## Space complexity
- `O(n)`

## Implemented in
- Python
- Go
- Java
- Rust
- C++
- TypeScript
