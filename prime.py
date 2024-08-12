def isprime(n):
    if(n==1 or n==0):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
start=int(input("enter value"))
end=int(input("enter end"))
for i in range(start,end+1):
    if isprime(i):
        print(i)        
