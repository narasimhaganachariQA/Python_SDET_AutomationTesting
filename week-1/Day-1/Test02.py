age=21 # int
name="narasimha" #string
is_pass=True  #bool
subject=["Maths","Science","English"] #list
credit=(1,2,3) # tuple
mentors={"A":"Maths"} #dictionary

a=10
print(isinstance(a,int))
print(isinstance(a,float))


#Type casting 
x="10"
print(type(x))
y=x
print(type(y))


x="10"
print(type(x))
y=int(x)
print(type(y))

# a=input("enter first number")
# b=input("enter second number")
# print(a+b) #output 1022

#type casting
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# print(a+b) #output 1022
#downcasting
a=10
b="10.5"
c=float(a)
d=float(b)
print(type(c))
print(type(d))


#example of implicit

p1=7
p2=5.22
p=p1+p2
print(type(p))