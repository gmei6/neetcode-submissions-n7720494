class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answers = []

        print(nums)

        for i in range(len(nums)):
            if i < len(nums) - 2:
                j = i + 1
                k = len(nums) - 1

                '''print("This is i ",  nums[i], i)

                print("This is j ",  nums[j], j)

                print("This is k ",  nums[k], k)

                print("")'''


                while j < k:
                    total = nums[i] + nums[j] + nums[k]

                    if total > 0:
                        k = k - 1
                    if total < 0:
                        j = j + 1
                    if total == 0:
                        if [nums[i] , nums[j] , nums[k]] not in answers:
                            answers.append([nums[i] , nums[j] , nums[k]])
                        j = j + 1
                        k = k - 1  
                            

            


        return answers