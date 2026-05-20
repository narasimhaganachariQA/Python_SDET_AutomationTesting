#memory managment
a=[1,2]
b=a
#[1,2] a,b list having two references
del a #a is delected but b has the reference (memory won't deleted)

#garabage collector
x=100
del x
#print(x) #deleting all ref and objects are called garabage collector 

x=10
id(x)
x=20 #old object may now or later GC will clear
id(20)
#id() is used for memorry address and also useful for debugging test data leaks


p=200
print(id(p))
