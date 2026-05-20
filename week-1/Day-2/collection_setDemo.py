python_team={"AI","PYTHON","SQL"}
cloud_team={"AWS","DOCKER","PYTHON"}

#find out all the skills 

print(python_team | cloud_team)
#common skills
print(python_team & cloud_team)

#skills of the python team without common skills
print(python_team - cloud_team)




