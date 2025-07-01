student = {"name": "Suraj", "course": "Python" ,"age":"20"}
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())


student.update({"name": "Sura"})
print(student)

print(student.pop("course"))
