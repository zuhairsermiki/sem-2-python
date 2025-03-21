import io
f=open('abc.txt','w')
# lis=list(map(str,input("enter your detail :").split()))
f.write(input("enter your detail:"))
f.close()
g=open('abc.txt','r')
text=g.read()
print(text)
g.seek(0)
print(".............................................................................")
line=g.readline()#read only single line
print(line)
g.seek(0)
print(".............................................................................")
lines=g.readlines()#read all lines one by one in form of list
print(lines)
print(".............................................................................")
g.close()
