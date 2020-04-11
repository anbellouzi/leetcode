class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        required = {}                        # stores index of a num
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i
    

if __name__ == "__main__":

    solution = Solution()
    nums = [3,2,4]
    target = 6
    result = solution.twoSum(nums, target)

    print(result)