use std::collections::HashSet;

fn contains_duplicate(nums: &[i32]) -> bool{
    let mut seen = HashSet::new();

    for &num in nums{
        if seen.contains(&num){
            return true;
        }
        seen.insert(num);

    }
    false
}

fn main() {
    let test_cases = vec![
        (vec![1,2,3,1], true),
        (vec![1,2,3,4], false),
        (vec![1,1,1,3,3,4,3,2,4,2], true),
    ];
    for (nums, expected) in test_cases {
        let result = contains_duplicate(&nums);
        println!("Input: {:?}, Output: {}, Expected: {}", nums, result, expected);
    }

}