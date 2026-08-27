class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_strs = ""
        for s in strs:
            encode_strs += f'{len(s)}#{s}'
        return encode_strs

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j+1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length
        return res