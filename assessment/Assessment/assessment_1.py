print("press 1 counsellor")
print("press 2 FOR faculty")
print("press 3 for student")
r=int(input("Enter role id:"))
if r==1:
    print("Add student")
elif r==2:
    print("Remove student")
elif r==3:
    print("View all student")
elif r==4:
    print("View specefic student")
else:
    print("Exit")

c=int(input("Enter a choice by consellor:"))
if c==1:
    stdata=dict()
    n=int(input("Enter number of pairs for dict:"))
    for i in range(n):
        key=input("Enter a key :")
        value=input("Enter a value:")
        stdata[key]=value
    print(stdata)

f1=open("demo.txt",'a')
a="1 Add marks to student"
b="2 view all student"
f1.write(f"Add marks to student{a}\n view all student{b}\n")
fc=input("Enter choice by Faculty:")

