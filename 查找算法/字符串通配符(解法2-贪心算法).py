'''
*te?t*.*
txt12.xls
~
false

*h
h
~
true
------------------
pRecord,sRecord:表示ui分别在ps和s串中的起始位置。
pindex,sindex:表示 分别在 ps和s串中遍历的位置。

模型1：
ps= '*u1*u2*u3...*un*'
s = 'a,b,c,u1,d,e,f,u2,...,z,x,y,un,1,2,3'
针对上述模型，只需要不断改变ui串在s串中的起点，直至匹配成功所有ui串 或 匹配失败。
假设，u1串在s串中的起点为0，匹配失败，则更改u1在s串的起点为1；匹配成功，则匹配下一个u2，直至结束。

模型2:
（1）ps的开头不是*；通过sRecord，pRecord=-1,来确定开头是不是*。如果不是，匹配失败则没有反悔机会；如果是，则修改sRecord起点和pRecord起点。
（2）ps的结尾不是*；只需要不断匹配s和ps串结尾字符，直到p为空或者p为*即可。

'''
def match(char1,char2):
    return char1.lower()==char2.lower() or (char1.isalnum() and char2=='?')

while True:
    try:
        flag=1
        ps,s=input(),input()
        pRight,sRight=len(ps),len(s)
        #看看ps是否是*结尾。若是*，则确定*在ps的起始位置并结束遍历；若不是，则不断匹配ps和s直至结束。
        while pRight>0 and sRight>0 and ps[pRight-1]!='*':
            if match(s[sRight-1],ps[pRight-1]):
                sRight-=1
                pRight-=1
            else:
                flag=0
                break
        if flag==0:
            print('false')
            continue
        if pRight==0:
            if sRight==0:
                print('true')
                continue
            else:
                print('false')
                continue
        #看看ps是不是*。若是*，则暴力枚举字符串s的每个位置作为起始点，并判断对应位置子串是否为ui；若不是，则不断匹配ps和s在开头处的字符即可。
        # 通过sRecord=-1和pRecord=-1，来判断开头处是否是*。
        sRecord,pRecord=-1,-1
        sindex,pindex=0,0
        endflag=1
        while sindex<sRight and pindex<pRight:
            if ps[pindex]=='*':
                pindex+=1
                pRecord=pindex  #在ps中,ui的起始位置
                sRecord=sindex  #在s中，假设的ui起始位置
            elif match(s[sindex],ps[pindex]): #ps的ui和s的ui的某个字符匹配成功，则移动当前遍历指针
                sindex+=1
                pindex+=1
            elif sRecord!=-1 and sRecord+1<sRight:  #如果ps开头为*，且两个字符没有匹配上，则调整ui在s串中的起始位置
                sRecord+=1   #假设不正确，修改ui在s中的起始位置
                sindex=sRecord  #s的遍历指针复位至重新修改的ui在s串中的起始位置处
                pindex=pRecord  #ps的遍历指针复位至ps中ui开始位置
            else:  #若ps开头不是*，两个字符匹配失败，则返回失败；若ps开头是*,则sRecord==sRight时，即ui在s串中不存在，匹配失败 或者 ps的开头不是*,
                endflag=0
                break
        if endflag==0 or not(all(ps[i]=='*' for i in range(pindex,pRight))):  #当endflag==0 或 ps的末尾不全为*时匹配失败
            print('false')
            continue
        print('true')
    except:
        break

'''    
    sindex = 0  # 字符串s遍历下标
    pindex = 1  # 匹配串ps遍历下标
    pRecord = 1  # 匹配串ps中  ui串出现的起始下标
    sRecord = 0  # 字符串s中 ui串出现的起始位置
    # 没有匹配上，说明sRecord值不对，需要修改
    flag = True
    while sindex < ls and pindex < lps:
        if ps[pindex] == '*':
            pindex += 1
            pRecord = pindex  # 记录ui在ps的开始位置
            sRecord = sindex  # 记录ui假设在s的开始位置
        elif match(ps[pindex], s[sindex]):  # 如果两个字符匹配，则匹配ui字符串中下一个字符
            pindex += 1
            sindex += 1
        elif sRecord + 1 < ls:  # 如果两个字符不匹配，说明 假设 ui在字符串s中的起始位置不正确，修改假设值
            sRecord += 1
            sindex = sRecord  # 复位，有可能是ps的ui中第一个字符 和 s的ui中第一个符匹配，第2个不匹配，所以需要复位
            pindex = pRecord  # 复位
        else:  # ui匹配失败
            flag = False
            break
    all(ps[pindex - 1:] == '*')
    if flag == False:
        print('false')
    else:
        if all(ps[i] == '*' for i in range(pindex - 1, lps)):
            print('true')
        else:
            print('false')'''