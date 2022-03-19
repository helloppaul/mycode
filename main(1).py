def compressString(S) :
    ch = S[0:1]  #压缩字符
    cnt = 0 #压缩字符的个数
    out=''
    ls = len(S)
    for c in S:
        if c==ch:
            cnt+=1
        else:
            out+=(ch+str(cnt))
            ch=c
            cnt=1
    out+=(ch+str(cnt))
    if len(out)>=ls:
        return S
    else:
        return out

r=compressString("bb")
print(r)