def rev(a):
    '''this function named rev() returns the reverse of the number a passed as an argument''' 
    r=0
    while a!=0:
        r=r*10+a%10
        a//=10
    return r
def isprime(b):
    '''this function named isprime() checks whether the number b passed as an argument is prime or not and returns in boolean accordingly'''
    y=0
    for x in range (2,b):
        if b%x==0:
            y=1
    if y==1:
        return False
    else:
        return True

n=int(input("enter the value of n:"))
c=0
i=3
p=0


if n==1:
    print("2")
elif n>1:
    while True:
        if ((isprime(i)==True) and i==rev(i)):
            c+=1
            p=i
        i+=1
        if c==n-1:
            print(p)
            break
                
        
    
    
