class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Let n be the size of nums
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        h_map_idx = dict()
        h_map_count = dict()

        for n in nums:
            if n in h_map_idx:
                h_map_idx[n] +=1  
            else: 
                h_map_idx[n] = 1

        for key, v in h_map_idx.items():
            if v in h_map_count:
                h_map_count[v].append(key)
            else:
                h_map_count[v] = [key]

        print(f"Index mapping: {h_map_idx}")
        print(f"Count mapping: {h_map_count}")

        ans = []
        while k > 0:
            maxx = max(h_map_count.keys())
            values = h_map_count[maxx]
            if k >= len(values):
                ans.extend(values)
                k-=len(values)
                del h_map_count[maxx]
            else:
                for i in range(k):
                    ans.append(values[i])
                k = 0
        return ans
    

test_cases = [
    {
        'nums':[1,2,2,3,3,3]
    }
]

o = Solution()
for test_case in test_cases:
    output = o.topKFrequent(nums=test_case['nums'], k=2)
    print(f"Input: nums={test_case['nums']} => Output: {output}")