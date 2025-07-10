class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = dict()

        for i,n in enumerate(nums):
            if n in index:
                index[n].append(i)
            else:
                index[n] = [i]

        print(f"Index mapping: {index}")

        for n in nums:
            remain = target - n

            if remain in index:
                print(f"Checking number: {n}, Remaining: {remain}")
                print(len(index[remain]), "occurrences of remaining number")
                if n == remain:
                    if len(index[remain]) >= 2:
                        return [index[remain][0], index[remain][1]]
                    else:
                        continue
                else:
                    return [index[n][0], index[remain][0]]

        return [-1,-1]
    
    def twoSumShort(self, nums: list[int], target: int) -> list[int]:
        index = dict()

        for i, n in enumerate(nums):
            remain = target - n
            if remain in index:
                return [index[remain], i]
            index[n] = i
    
test_cases = [
    {
        'nums':[3,2,4], 'target': 6, 'result': [1,2]
    },
    {
        'nums':[3,3], 'target': 6, 'result': [0,1]
    }
]

o = Solution()
for test_case in test_cases:
    output = o.twoSumShort(nums=test_case['nums'], target=test_case['target'])
    print(f"Input: nums={test_case['nums']}, target={test_case['target']} => Output: {output}")