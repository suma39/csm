n=int(input())
rev=0
temp=n
while n>0:
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
print(rev)
if(temp==rev):
    print("palindrome")
else:
        print("not palindrome")
