class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answers = []

        print(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k = k - 1
                if total < 0:
                    j = j + 1
                if total == 0:
                    # Just append directly. The logic below guarantees uniqueness.
                    answers.append([nums[i], nums[j], nums[k]])
                    
                    j = j + 1
                    k = k - 1
                    
                    # While the new j is the same as the old j, keep moving!
                    while j < k and nums[j] == nums[j - 1]:
                        j = j + 1
                        
                    # While the new k is the same as the old k, keep moving!
                    while j < k and nums[k] == nums[k + 1]:
                        k = k - 1

        return answers