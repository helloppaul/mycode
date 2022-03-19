'''对字符串中的所有单词进行倒排。
说明：
1、构成单词的字符只有26个大写或小写英文字母；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；

for key in range(97,122):
    d[chr(key)] = 1

for key in range(65,90):
    d[chr(key)] = 1

输入：
I am a student
输出：
student a am I

输入：
$bo*y gi!r#l
输出：
l r gi y bo
'''
d={'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1,'z':1,'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1, 'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1,'Z':1}
while True:
    try:
        s=input()
        r=''
        word=''
        i=0
        for v in s:
            if v in d:
                word += v
            else:
                if s[i-1] in d:
                    r=word+' '+r
                    word = ''
            i+=1
        r = word + ' ' + r
        print(r)
    except:
        break
