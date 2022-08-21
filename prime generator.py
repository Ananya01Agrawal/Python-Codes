
def checkPrime(num):
    if num==0 or num==1 :
        return False
    elif num==2 :
        return True
    elif num%2==0 :
        return False
    else :
        i=2
        while(i*i<=num):
            if(num % i==0):
                return False
            i=i+1
        return True
        
            
    

T = int(input())
while(T>0):
    l = [int(i) for i in (input().split())]
    x = l[0]
    y = l[1]
    
    for i in range(x,y+1):
        if (checkPrime(i)):
            print(i,end=" ")
            
    print()
    
    T -= 1
