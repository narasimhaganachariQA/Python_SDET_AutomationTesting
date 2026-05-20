student={"narasimha","java-selenium"}
print(student)

# read operation

for s in student:
    print(s)

#updating
student.add("9999")
student.update(["Ab","Bc"])

#deleting
#student.remove("A")
student.pop()
print(student)

a={1,2,3,6}
b={5,6,7}
print(a|b)
#intersession
print(a&b)
#difference
print(a-b)

#symetric difference
print(a^b)

#unpacking or spread *

s={*a, *b}
print(s)

#unpacking or spread * without duplicates
#s={*a}



