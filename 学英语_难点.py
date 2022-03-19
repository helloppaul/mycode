'''486669'''
def numberTo(s):
    ls=len(s)
    left = ls % 3

    flag=''
    if 3<ls<7:
        flag = ' thousand '
    elif 7<=ls<10:
        flag = ' million '
    elif 10<=ls<13:
        flag = ' billion '

    res=''
    if left==1:
        res += Map0[s[0]] + flag
    elif left==2:
        if s[0]=='0':  #403(03部分)
            return Map0[s[1]]
        if s[0:2] in Map0 :
            res += Map0[s[0:2]] + flag
        elif s[0] in Map1 and s[1] in Map0 :
            res += Map1[s[0]]+' '+Map0[s[1]] + flag
        else :
            res += Map1[s[0]] + flag
    else:
        left=3
        if s[0] == '0':  #8,088(088部分)
            res += numberTo(s[1:3])+flag
        elif s[1:3]=='00':
            res +=  Map0[s[0]] + ' ' + 'hundred' + flag
        else:
            res += Map0[s[0]] + ' ' + 'hundred' + ' and ' + numberTo(s[1:3])+flag
    if ls>3 :
        res+= numberTo(s[left:])
    return res
'''1403523'''

Map0={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten',
      '11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
Map1={'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}

while True:
    try:
        snum=input()
        print(numberTo(snum))
    except:
        break