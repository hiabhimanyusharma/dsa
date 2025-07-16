class Solution:

    def encode(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        
        return f"|{'|'.join(strs)}"

    def decode(self, s: str) -> list[str]:
        if len(s) == 0:
            return []

        return s.split('|')[1:]

test_cases = [
    {
        'strs':["act","pots","tops","cat","stop","hat"]
    },
    {
        'strs':["neet","code","love","you"]
    },
    {
        'strs':["a"]
    },
    {
        'strs':[]
    },
    {
        'strs':[""]
    }
]

o = Solution()
for test_case in test_cases:
    output = o.encode(strs=test_case['strs'])
    print(f"Input: strs={test_case['strs']} => Output: {output}")
    decoded_output = o.decode(s=output)
    print(f"Decoded Output: {decoded_output}")