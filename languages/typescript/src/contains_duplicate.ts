const testCases: Array<{ nums: number[]; expected: boolean }> = [
  { nums: [1, 2, 3, 1], expected: true },
  { nums: [1, 2, 3, 4], expected: false },
  { nums: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], expected: true },
];

for (const testCase of testCases) {
  const result = containsDuplicate(testCase.nums);
  console.log(
    `nums=${JSON.stringify(testCase.nums)} -> result=${result}, expected=${testCase.expected}`,
  );
}

function containsDuplicate(nums: number[]): boolean {
  const seen = new Set<number>();
  for (const num of nums) {
    if (seen.has(num)) {
      return true;
    }
    seen.add(num);
  }
  return false;
}
