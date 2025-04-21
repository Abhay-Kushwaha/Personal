import random
print("\nHello! I'm NumNator. I will guess the number you choose.\nType 'yes' or 'no' for input")
a=random.randrange(1,6)
b=random.randrange(11,51)
c=random.randrange(6,11)
d=random.randrange(51,71)
e=random.randrange(71,100)
print("Choose any one number in your mind : ",a,b,c,d)
S1=[e,b,c,a]
S2=[b,a,d,e]
S3=[d,e,b,c]
S4=[a,c,d,e]
S5=[c,b,a,d]
print("Is your number present in ",S1,end='')
a1=str(input(": "))
if (a1.lower()=="yes"):
    print("Is your number present in ",S2,end='')
    a2=str(input(": "))
    if (a2.lower()=="yes"):
        print("Is your number present in ",S3,end='')
        a3=str(input(": "))
        if (a3.lower()=="yes"):
            print("Is your number present in ",S4,end='')
            a4=str(input(": "))
            if (a4.lower()=="yes"):
                print("Is your number present in ",S5,end='')
                a5=str(input(": "))
                if (a5.lower()=="yes"):
                    print("Naughty Boy....Playing with me.")
                elif(a5.lower()=="no"):
                    print("Your number is:",e)
                else:
                    print("No other input allowed other  than 'yes' and 'no'")
            elif(a4.lower()=="no"):
                print("Your number is:",b)
            else:
                print("No other input allowed other  than 'yes' and 'no'")
        elif(a3.lower()=="no"):
            print("Your number is:",a)
        else:
            print("No other input allowe other than 'yes' and 'no'")
    elif(a2.lower()=="no"):
        print("Your number is:",c)
    else:
        print("No other input allowed other  than 'yes' and 'no'")
elif(a1.lower()=="no"):
    print("Your number is:",d)
else:
    print("No other input allowed other  than 'yes' and 'no'")