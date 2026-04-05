# Polyglot Works

Learning data structures and algorithms across multiple languages.

## Planned languages

- Python
- Go
- Java
- Rust
- C++
- TypeScript

## Project structure

- `languages/` -> one folder per language
- `tools/` -> helper scripts
- `benchmarks/` -> benchmark config and results
- `problems/` -> problem statements and notes
- `templates/` -> reusable templates for new problems
- `PROGRESS.md` -> personal progress tracker

## Start the environment

```bash
make build
make up


make shell
make benchmark
make run-python
make run-go
make run-java
make run-rust
make run-cpp
make run-ts
```

## Suggested Roadmap

### Arrays and Hashing

- `valid_anagram`
- `group_anagrams`
- `top_k_frequent_elements`
- `product_except_self`

### Sliding Window

- `longest_substring_without_repeating`

### Stack

- `valid_parentheses`
- `daily_temperatures`

### Linked List

- `reverse_linked_list`

### Binary Search

- `binary_search`

### Trees and Graphs

- `maximum_depth_binary_tree`
- `number_of_islands`

### Intervals and Heaps

- `merge_intervals`
- `k_closest_points_to_origin`

### Dynamic Programming

- `coin_change`

## Useful commands

```bash
make shell
make benchmark
make benchmark PROBLEM=two_sum
make ts-install
make run-python
make run-python PROBLEM=two_sum
make run-go PROBLEM=two_sum
make run-java PROBLEM=two_sum
make run-rust
make run-cpp PROBLEM=two_sum
make run-ts PROBLEM=two_sum
```
