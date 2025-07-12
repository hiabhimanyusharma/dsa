class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Let m be size of strs and n be the maximum length of a string in strs
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
        hash_map = dict()
        for s in strs:
            simple_map = [0]*26
            for alpha in s:
                simple_map[ord(alpha) - ord('a')] += 1

            if str(simple_map) in hash_map:
                hash_map[str(simple_map)].append(s)
            else:
                hash_map[str(simple_map)] = [s]

        return [list(group) for group in hash_map.values()]

test_cases = [
    {
        'strs':["act","pots","tops","cat","stop","hat"]
    },
    {
        'strs':["eat","tea","tan","ate","nat","bat"]
    },
    {
        'strs':["a"]
    }
]

o = Solution()
for test_case in test_cases:
    output = o.groupAnagrams(strs=test_case['strs'])
    print(f"Input: strs={test_case['strs']} => Output: {output}")