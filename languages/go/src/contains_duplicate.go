package main

import "fmt"

func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)

	for _, num := range nums {
		if seen[num] {
			return true
		}
		seen[num] = true
	}

	return false
}

func main() {
	testCases := []struct {
		nums	 []int
		expected bool
	}{
		{[]int{1, 2, 3, 1}, true},
		{[]int{1, 2, 3, 4}, false},
		{[]int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
	}

	for _, tc := range testCases {
		result := containsDuplicate(tc.nums)
		fmt.Printf("num=%v -> result=%v (expected=%v)\n", tc.nums, result, tc.expected)
	}
}