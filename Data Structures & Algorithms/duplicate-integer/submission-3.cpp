#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> dict;
        for (int i = 0; i < nums.size(); i++) {
            if (dict.find(nums[i]) == dict.end()) {
                dict.insert(nums[i]);
            } else {
                return true;
            }
        }
        return false;
    }
};