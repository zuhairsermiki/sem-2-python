print("lamda function and map")
x=1
y=2
mx=lambda x,y:x if x>y else y
print(mx(10,15))
mx=lambda x: x*4

# map {list[m,n,p],function,f() ->MAP-> new list [f(m),f(n),f(p)]}
n=[4,3,2,1]
p=[4,5,10,13]

print(list(map(lambda x,y :x*y ,n,p)))
