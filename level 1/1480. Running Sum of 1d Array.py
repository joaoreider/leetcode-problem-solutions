

# My solution (35ms)
class Solution:

    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(0, len(nums)):

            if i == 0:
                result.append(nums[i])
            else:
                result.append(nums[i]+result[i-1])
        
        return result



# Best Solution (19ms)
class Solution:

    def runningSum(self, nums: list[int]) -> list[int]:

        sum = 0

        arr = []

        for n in nums:

            sum += n

            arr.append(sum)

        return arr
