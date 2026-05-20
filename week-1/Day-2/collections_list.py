student=["Nara","simha","leela"]

print("\n =====Student managment System===")
print("1. Add student")
print("2.view student")
print("3.update student")
print("4.Delete student")
print("5.Exit")
while True:
    choice = input("Enter choice : ")

    #create
    if choice =="1":
        name =input("Enter Student Name : ")
        student.append(name)
        print("student added successfuly")

#read
    elif choice=="2":
        print("\n Student list")
        for s in student:
            print(s)
    #print(student)

    elif choice=="3":
        old_name=input("Enter old Name")
        new_name=input("Enter new Name")
        index=student.index(old_name)
        student[index]=new_name

        print("Student details updated ")

    elif choice=="4":
        remove_Name =input("removal Name")
        student.remove(remove_Name)
        print(student)

    elif choice=="5":
        print("program Ended")

        break

    else:
        print("Invalid choice")


