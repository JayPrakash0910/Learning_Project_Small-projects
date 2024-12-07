from secrets import choise


def add(a, b):
    ans = a + b
    print((a)+ " + " (b) + "="+(ans)+"\n")
def sub(a, b):
    ans = a - b
    print((a)+ " - " (b) + " = " +(ans)+"\n")
def mul(a, b):
    ans = a * b
    print((a)+ " * " (b) + " = " + (ans)+"\n")
def div(a, b):
    ans = a / b
    print((a)+ " / " (b) + " = " + (ans)+"\n")
while True:
 print("A.addition")
 print("B.substract")
 print("C.multiple")
 print("D.division")
 print("E.exit")

choise =input("input your choise : ")

if choise == "a" or choise =="A":
    print("addition")
    a=int(input("input first number : "))
    b=int(input("input first number : "))
    add(a,b)

elif choise == "b" or choise =="B":
    print("asubstract")
    a=int(input("input first number : "))
    b=int(input("input first number : "))
    sub(a,b)
    
elif choise == "c" or choise =="C":
    print("multiple")
    a=int(input("input first number : "))
    b=int(input("input first number  : "))
    mul(a,b)
elif choise == "d" or choise =="D":
    print("division")
    a=int(input("input first number : "))
    b=int(input("input first number : "))
    add(a,b)

elif choise == "e" or choise =="E":
    print("program are khtam ")
    quit()
        