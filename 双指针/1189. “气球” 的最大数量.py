class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bs={'b':0,'a':0,'l':0,'o':0,'n':0}
        clen=len(text) #字符串长度
        for i in range(clen):
            if text[i] in bs:
                bs[text[i]]+=1
        bs['l']//=2
        bs['o']//=2
        min_=bs['b']
        for i in bs:
            if bs[i]<min_:
                min_=bs[i]
        return min_
