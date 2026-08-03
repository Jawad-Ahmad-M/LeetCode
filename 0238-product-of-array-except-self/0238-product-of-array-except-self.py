import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        left = []
        right = []

        product = 1
        for x in range(len(nums)):
            left.append(product)
            product *= nums[x]
        # print(left)

        product = 1
        for x in range(len(nums)-1 , -1 , -1):
            right.append(product)
            product *= nums[x]
        # print(right)
            

        for x in range(len(nums)):
            new_list.append(left[x] * right[len(nums) - 1 - x])

        

        
        


        return new_list
