#create a log 

logs=[{"api":"login","time":2.5},
      {"api":"payment","time":1.2},
      {"api":"search","time":3.1}]

sorted_log=sorted(logs,key=lambda x: x['time'])
print(sorted_log)

c=lambda a,b:(a**2)+(b**2)+(2*a*b)

print(c(2,3))
