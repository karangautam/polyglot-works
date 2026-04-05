#include <iostream>
#include <vector>
#include <unordered_set>


bool containsDuplicate(const std::vector<int>& nums){
    std::unordered_set<int> seen;
    for (int num: nums){
        if (seen.find(num) != seen.end()){
            return true;
        }
        seen.insert(num);

    }
    return false;

}

int main(){
    std::vector<std::pair<std::vector<int> ,bool>> testCases = {
        {{1, 2, 3, 1}, true},
        {{1, 2, 3, 4}, false},
        {{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true}
    };
    
    for (const auto& testCase : testCases){
        const auto& nums = testCase.first;
        bool expected = testCase.second;
        bool result = containsDuplicate(nums);
                std::cout << "nums=[";
        for (size_t i = 0; i < nums.size(); i++) {
            std::cout << nums[i];
            if (i + 1 < nums.size()) {
                std::cout << ", ";
            }
        }
        std::cout << "] -> result=" << (result ? "true" : "false")
                  << ", expected=" << (expected ? "true" : "false") << std::endl;
    }

    return 0;

    }
