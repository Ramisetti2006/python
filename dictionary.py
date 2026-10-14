student={"Roll NO":73,"Name":"Supriya","branch":"MCA","CGPA":9.0}
print(student)
#Accessing Dictionary Elements
print(student["Name"])
print(student["CGPA"])
#Adding New Elements
student["Number"]=265444582
print(student)
#Updating Dictionary
student["Name"]="R Supriya"
print(student)
#Delete an Element
del student["Number"]
print(student)
#Dictionary Traversal
for key,value in student.items():
    print(key,"=",value)


