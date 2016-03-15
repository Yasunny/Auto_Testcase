#coding=utf-8
def Fn(n):
    if n==1:
        return 1
    else:
        return n*Fn(n-1)

print(Fn(3))

def Fn(m,n):
    if n==m:
        return 1
    elif n>m:
        return error
    elif n==m:
        s=1
        while n>0:

            s=s*n
            n=n-1
        return s
    else:
        return m*


print(Fn(3,3))