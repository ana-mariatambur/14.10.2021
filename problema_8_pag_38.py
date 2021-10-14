sir=str(input('Introduceti caracterele separate prin spatiu:'))
n=''
u=0
r=''
urmator=0
sir=sir.replace(' ',' ')
for x in range(0,len(sir)): 
    u=sir[x].isupper()
    if u==True:
        if sir[x]!=' ' and sir[x]!='Z':
            urmator=chr(ord(sir[x])+1)
            r=sir.replace(sir[x], urmator)
            n+=r[x]
        else:
            n+=sir[x]
    else:
        exit()
n=' '.join(n)
print('a)',n)
n=n.replace('Z','A')
print('b)',n)
n=n.replace(' ','-')
print('c)',n)