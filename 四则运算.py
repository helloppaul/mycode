exp=input()
exp=exp.replace('{','(',10)
exp=exp.replace('}', ')',10)
exp=exp.replace('[', '(',10)
exp=exp.replace(']', ')',10)
print(int(eval(exp)))

