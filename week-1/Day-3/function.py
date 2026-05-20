

# #multiple return
# def student():
#     return "na",21
# name,age=student()
# print(name)


# #type hint
# def add(a:int,b:int) -> int:
#     return a+b

# print(add(6,7))


# #Nested function:

# def outer():
#     #print("outer function")
#     def inner():
#         print("inner function")
#     inner()
# outer()

# #Function with default parameter

# def greet(name="Guest"):
#     print("Welcome", name)
#greet()
#greet("Arun")

#keyword arguments
# def student(name,age):
#     print(name,age)

# student(age=12,name="nara")
# student("nara",22)

#example:
# def a(name):
#    # print(name*name)
#    return name*name
# #v=a(5)
# #print(v)
# print(a(5))

def a(va):
   print(va)

#a(5)
print(a(5))

#*args

# def log_failures(*test_ids):
#     for tid in test_ids:
#         print(f"Test {tid} failed")

# log_failures(101,102,103,104)

# #**KWARGS

# def run_tests(*tags,**filters):
#     print(f"Tages :{tags}")
#     print(f"Filters : {filters}")

# run_tests(
#     "smoke",
#     "regression",
#     env="prod",
#     priority="high"
# )

#Lambda Expression:

# logs=[
#     {'time':12.3,'msg':'ek'},
#     {'time':3.1,'msg':'fail'}
# ]

# sorted_log=sorted(logs,keyss=lambda x: x['time'])

#------------------------------------------------------------------------------------------------
#normal function
# def add(a,b):
#     return a+b
# print(add(2,5))

# #convering above function into lambda

# add = lambda a,b:a+b


# print(add(2,4))
