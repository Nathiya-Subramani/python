
students = {
    "arun_01":[90,95,88,92,100],
    "vijay_02":[100,65,88,90,100],
    "madhan_03":[90,95,88,92,85],
    "madhan_04":[100,65,88,90,100]
}


total = sum(students["madhan_03"])
print(total)

lowest = min(students["madhan_04"])
print("madhan_04:",lowest)

marks = students.get("arun_01")
print(marks)

print(students["arun_01"][2:5:1])


# student_total(students,"arun_01")

# subjects = ["tamil","english","maths","chemistry","physics"]
