def trans(n):
    return (n*n+2)/2
def retrans(p):
    return ((p*2-2)**0.5)
    
numbers=list(map(int ,input("enter a multiple numbers separte by space ").split()))
result=list(map(lambda x:trans(x),numbers))
print(result)
orig=list(map(lambda x: retrans(x),result))
print(orig)


