# students={
#     "zuhair":(1,[2,4,6,8]),
#     "HUssIAN":(2,[1,3,6,7]),
#     "SERMIKI":(3,[3,6,9,2]),
#     "ali":1
# }
# print(students.items())
# print(students["zuhair"])
# students.update({"zuhair":500})
# print(students)
def up(n):
    n="*"
    return n
dic={
    1:"zuhair",
    2:"hussain",
    3:"sermiki"
}
result=map( lambda x : up(x),dic.values()) 
dic=dict(zip(dic.keys(), result ))
print(result)
print(dic.items())