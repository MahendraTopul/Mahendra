
#Arithmetic operators

a,b,c=10,20,30

print("10+20=",a+b)
print("10-20=",c-b)
print("10*20=",a*b)
print("30/10=",c/a)

#Comparison operators

print(" a>b",a>b)
print(" a<b",a<b)
print(" a==b",a>b)
print("a!=b",a!=b)

#Logical operators

a=True
b=False

print("a and b is ",a and b)
print("a or b is ",a or b)
print("not b is ",not b)

#Identity operators

x1=5
x2="Hii"
x3=[4,5,6]
y1=5
y2="Hii"
y3=[4,5,6]

print("x1 is not y2",x1 is not y2)
print("x1 is not y1",x1 is not y1)
print("x2 is y2",x1 is y2)
print("x3 is y2",x3 is y3)

#Membership operators

n1="Hello"
n2={1:"a",2:"b"}

print("H" in n1)
print("Hello" not in n1)
print(1 in n2)
print("a" in n2)