num=int(input('enter a num'))
fact=1
if(num<0):
    print('negative')
elif num==0:
    print('fact of o is')
else:
    for i in range(1,num+1):
     fact=fact*i
    print('fact of',num,'is' ,fact)
                
