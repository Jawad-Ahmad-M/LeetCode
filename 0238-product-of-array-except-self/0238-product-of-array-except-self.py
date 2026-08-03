import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # Prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        prev_suffix = 1

        # Suffix products
        for i in range(n - 2, -1, -1):
            prev_suffix *= nums[i + 1]
            ans[i] *= prev_suffix

        return ans
