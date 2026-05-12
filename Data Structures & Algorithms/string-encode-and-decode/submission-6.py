class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += f"{len(s)}#{s}"
        return ans

    def decode(self, s: str) -> List[str]:
        ptr = 0
        ans = []
        while ptr < len(s):
            char = ""
            while s[ptr] != "#":
                char += s[ptr]
                ptr += 1
            
            ans.append(s[ptr+1:ptr+int(char)+1])
            ptr += int(char)+1

        return ans

