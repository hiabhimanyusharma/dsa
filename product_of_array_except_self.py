class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre_product = []
        for i in range(len(nums)):
            if i == 0:
                pre_product.append(1)
            else:
                pre_product.append(pre_product[i - 1] * nums[i - 1])

        post_product = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post_product.append(1)
            else:
                post_product.append(post_product[-1] * nums[i + 1])

        result = []
        for i in range(len(nums)):
            result.append(pre_product[i] * post_product[-1 - i])

        return result

test_cases = [
    {
        'nums':[1,2,3,4]
    },
    {
        'nums':[-1,1,0,-3,3]
    },
    {
        'nums':[6,9]
    }
]

o = Solution()
for test_case in test_cases:
    output = o.productExceptSelf(nums=test_case['nums'])
    print(f"Input: nums={test_case['nums']} => Output: {output}") 

# [1, 1, 2, 6] [24, 12, 4, 1]
# [-1, -1, -1, 0, 0] [0, 0, -9, 3, 1]