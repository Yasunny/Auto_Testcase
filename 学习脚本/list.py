L='123'

for i in L:

    if i=='.':
       L=L.replace('.','')
    else:
        pass
    print(i)
print(L)


s="|DF|A3"
b=s.split("|")
print(b)
print(len(b))