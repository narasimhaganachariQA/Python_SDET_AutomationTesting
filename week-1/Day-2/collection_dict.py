# #dictonary

# contact ={
#     "nara":"9533",
#     "subbu":"1234"
# }

# print(contact)
# #creating dict in second approach
# con=dict(id="nara",name="narasimha")
# print(con)

student={"name":"rahul",
         "Age":20,
         "mail":"rahuk12@gmail.com",
         "subject":"CSE"
         }

# # print(student["name"])
# # #update
# # student["Age"]=25
# # print(student)
# # #delet
# # del student["Age"]
# # print(student)

# print(student.keys())
# print(student.items())
# print(student.values())

# print(student.get("wer"))
# student.update({"name":"simha"})
# print(student)
# print(student.pop("name"))
# #clear
# #student.clear()

#Neted dict
math_core={("csk","MI"):182}
print(math_core["csk","MI"])

test_data={
    101:{"status":202,
            "msg":"success"
         } ,
    102:{"status":500,
         "msg":"success"
         }
}

print(test_data[101]["status"])

