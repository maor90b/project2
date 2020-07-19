keys=[]
val=[]
dict1={}
for i in range(5):
    name=input("enter name: ")
    grade=int(input("enter grade: "))
    keys.append(name)
    val.append(grade)
    dict1[name]=grade
print(dict1)
print(sum(dict1.values()))
