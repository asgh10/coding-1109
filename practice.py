student = {
    "name": "현빈",
    "age": 17,
    "major": "소프트웨어개발과"
}
print(student["name"])
print(student["major"])

student["age"] = 18
student["major"] = "백엔드 개발자"

print(student["age"])
print(student["major"])

def print_student(student):
    print("이름:", student["name"])
    print("나이:", student["age"])

print_student(student)

student1 = {"name": "현빈", "age": 17}
student2 = {"name": "철수", "age": 18}

def print_student(student):
    print("이름:", student["name"])
    print("나이:", student["age"])

print_student(student1)
print_student(student2)