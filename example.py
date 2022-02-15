n="2312179862310199501872379231018117937"
       
res=[]
while n!=0:
    x=n[-2:]
    if int(x[::-1])==32 or (int(x[::-1])>64 and int(x[::-1])<91) or (int(x[::-1])>96 and int(x[::-1])<123):
        res.append(int(x[::-1]))
        n=str(int(n)//100)
    x=n[-3:]
    if int(x[::-1])==32 or (int(x[::-1])>64 and int(x[::-1])<91) or (int(x[::-1])>96 and int(x[::-1])<123):
        res.append(int(x[::-1]))
        n=str(int(n)//1000)
    if int(n)==0:
        break

ans=[]
for i in res:
    ans.append(chr(i))
print(''.join(ans))
