#length of the string
#replace is with are
#add SDET after python
#split senstace two by using and

str1="this is B1 TR and python training is going on"

print(len(str1))
#print(str1.replace("is","are"))

updated_list =[]
for w in str1:
    if w=="is":
        updated_list.append("are")

    else:
        updated_list.append(w)
new_text=" ".join(updated_list)
print(updated_list)

