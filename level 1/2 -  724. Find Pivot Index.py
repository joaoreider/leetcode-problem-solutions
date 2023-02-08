
# My solution (7196 ms)
# Main learning: Dont repeat the function on each iteration. Assigns to a variable aobot the beginning
class Solution:

    def pivotIndex(self, nums: list[int]) -> int:
        
        self.pivot_index = -1

        for i in range(len(nums)):


            if i == 0:
                self.sumleft = 0
                self.sumright = sum(nums) - self.sumleft  - nums[i]

            
            elif i == (len(nums)-1):
                self.sumleft += nums[i-1]
                self.sumright = 0


            else:
                self.sumleft += nums[i-1]
                self.sumright = sum(nums) - self.sumleft  - nums[i]
                
            
           
            if self.sumleft == self.sumright:
                self.pivot_index = i
                break
        
        return self.pivot_index



# Best solution (181 ms)
class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0
        for i, x in enumerate(nums):
            if leftSum == (total - leftSum - x):
                return i
            leftSum += x
        return -1



if __name__ == '__main__' :
    nums = [-1,-1,0,1,1,0]
    r = Solution().pivotIndex(nums=nums)
    print(r)

    

            

        

