a=str(input("Enter your name: "))
a=a.lower()
L1=[]
b=str(input("Enter your Crush's name: "))
b=b.lower()
for i in a:
    L1.append(i)
for j in b:
    if (j in L1):
        L1.remove(j)
    else:
        L1.append(j)

x=len(L1)
print(x)
y=6
L2=["F","L","A","M","E","S"]
for i in range(0,5,1):
    pos=(x%y)-1
    L2.pop(pos)
    print(L2)
    y=y-1
    x=x+i*1

# for i in range(0,5,1):
#     pos=x-(y*(x//y))-1
#     L2.pop(pos)
#     print(L2)
#     y=y-1
#     x=x+pos

if L2[0] == 'F':
    print("Friends")
elif L2[0] == 'L':
    print("Love")
elif L2[0] == 'A':
    print("Affection")
elif L2[0] == 'M':
    print("Marriage")
elif L2[0] == 'E':
    print("Enemy")
elif L2[0] == 'S':
    print("Siblings")