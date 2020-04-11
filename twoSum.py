"""
Restate: Find two numbers that when added together, can sum up to a target number. Return indexes of those two values. 
Questions: Are numbers sorted? is there negatives? Are there dublicates? Can target be one number?
Assumptions: All numbers are integer values.
Solutions: Loop over list of num and store nums in a dict with indexes as values. Check if target - current number 
            is already is dict -> return indexes else store current number and its index in dict. 
Explain: Time efficiency -> loop over nums once and return a result
Tradeoff: Space complexity -> storing nums in a dict will consume storage and if nums are long, can take longer time.
Improvments: Store numbers that are less or equal to target, avoiding unnecessary numbers 
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        required = {}                        # nums with their corresponding index required for sum 
        for i in range(len(nums)):
            if target - nums[i] in required: # check if current number - target is already stored
                return [required[target - nums[i]], i]
            else:   
                required[nums[i]] = i       # stores nums as keys and indexes as values 

if __name__ == "__main__":

    solution = Solution()
    nums = [3,2,4]
    target = 6
    result = solution.twoSum(nums, target)

    print(result)