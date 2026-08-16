class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string)) + "#" + string
        
        return encode

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1

            length = int(s[i:j])

            result.append(s[j+1:j+length+1])

            i = j + length + 1
        
        return result
