def zuhair( n):
    
    
    if n<=1:
        return 0
    elif n==2:
        return 1
    else:
        return zuhair(n-1)+zuhair(n-2)
        
        
        
    
def rec(n):
    if n>=1:
        return (n*zuhair(n-1))   
    else:
        return 1
    
# name="zuhair hussain sermiki"
# print(name[:len(name)-2])
p=int(input("enter a number:",))
print(zuhair(p))
q=int(input("enter a number:",))
print(rec(q))
