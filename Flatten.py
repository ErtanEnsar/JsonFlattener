from JsonFlattener import JsonFlattener

#Create Class
JsonFlattener=JsonFlattener()
#Take Input
data=JsonFlattener.data_loader_sanitizer()
#Flatten Json Object
data=JsonFlattener.flatten(data)
print(data)
