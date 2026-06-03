class Solution:
    """
    [长度] + [特殊字符] + [实际字符串]

    编码示例：
    假设输入：["neet", "co#de", "you"]

    处理 "neet"：长度为 4。编码为 "4#neet"

    处理 "co#de"：长度为 5。编码为 "5#co#de"

    处理 "you"：长度为 3。编码为 "3#you"

    最终组合成的大字符串是："4#neet5#co#de3#you"

    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)

            i = j + 1 + length
        return res
