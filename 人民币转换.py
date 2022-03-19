# '1234'
# '1,2345 一万两千三百四十五'
# '123,2345'
def f(sn):  #处理整数
    lsn=len(sn)
    if lsn>=9:
        if sn[:2] == '00':
            return f(sn[lsn-9+1:])
        elif sn[0] == '0':
            return '零' + f(sn[lsn-9+1:])
        return f(sn[:lsn-9+1])+ "亿" + f(sn[lsn-9+1:])
    elif lsn>=5:
        if sn[:2] == '00':
            f(sn[lsn - 5 + 1:])
        elif sn[0] == '0':
            return '零' + f(sn[lsn - 5 + 1:])
        return  f(sn[:lsn - 5 + 1])  + "万" + f(sn[lsn - 5 + 1:])
    elif lsn>=4:
        if sn[:2] == '00':
            return f(sn[lsn - 4 + 1:])
        elif sn[0] == '0':
            return '零' + f(sn[lsn - 4 + 1:])
        return  f(sn[:lsn - 4 + 1])  + "仟" + f(sn[lsn - 4 + 1:])
    elif lsn>=3:
        if sn[:2]=='00' :
            return f(sn[lsn - 3 + 1:])
        elif sn[0]=='0':
            return '零'+ f(sn[lsn - 3 + 1:])
        return f(sn[:lsn - 3 + 1]) + "佰" + f(sn[lsn - 3 + 1:])
    elif lsn >= 2:
        if sn[:2] == '00':
            return ''
        return (M[int(sn[0])] if int(sn[0])>1 else '') + "拾" + (M[int(sn[1])] if int(sn[1])>0 else '')
    else:
        return M[int(sn)]
def g(sn):  #处理小数
    if sn[:2]=='00':
        return '整'
    if sn[0]=='0':
        return M[int(sn[1])]+'分'
    if sn[1]=='0':
       return M[int(sn[0])]+'角'
    return M[int(sn[0])]+'角'+M[int(sn[1])]+'分'

'''151121.15
30105000.00
'''
while True:
    try:
        M=['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
        round,d=input().split('.')
        rf=f(round)
        if rf=='零':
            print('人民币'+g(d))
        else:
            print('人民币'+rf+'元'+g(d))
    except:
        break