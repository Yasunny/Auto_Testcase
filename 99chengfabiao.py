#coding=utf-8

'''def multi(x,y)
    return x*y
'''

for i in range (1,10):
    for j in range (1,i+1):

        print(j,"*", i, "=",i*j,"\t",end='')
        #print ("%d * %d = %d\t" %(i,j,i*j))
    print("\n")
print("\nDone!")


