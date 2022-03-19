'''
示例1
输入：
Ihave1nose2hands10fingers
输出：
0112Iaadeeefghhinnnorsssv
'''

while True:
    try:
        s=sorted(input())
        print(''.join(s))
    except:
        break