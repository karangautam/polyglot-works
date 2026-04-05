def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    :param nums: List[int] - The input array of integers.
    :return: bool - True if any value appears at least twice, False otherwise.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    for nums, expected in test_cases:
        result = contains_duplicate(nums)
        print(f"nums={nums} -> result={result}, expected={expected}")
