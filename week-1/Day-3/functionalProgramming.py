from functools import reduce
#Functional programming
#map(fun, itr)

# marks=[40,50,60,70]

# percentage =list(map(lambda x:x/100,marks))
# print(percentage)

#filter(fun, itr)

# salary =[50000,77000,90000,75000]

# highdt=list(filter(lambda x:x >=70000,salary))
# print(highdt)
# sortted=list(sorted(filter(lambda x:x >=70000,salary)))
# print(sortted)


#reduce() - combine data

# salary =[111111,222222,333333,444444]
# total=reduce(lambda a,b :a+b,salary)
# print(total)

#list comprihensions
numbers=[1,2,3,4,5]
square=[n*n for n in numbers]
even_no =[x for x in numbers if x%2 ==0  ]

print(even_no)
print(square)


#Nested list comprihentions

matrix=[[1,2],[3,4],[5,6],[7,8]]

flate=[num for row in matrix for num in row]
print(flate)
