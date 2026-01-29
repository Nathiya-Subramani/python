# get marks per for all 5 subjects
# calculate total
# calculate student grade 
# find top score
# find pass are fail
# find subject with centum score
# calculate percentage 
# calculate cutoff (maths,physics,chemistry)
# # student data - dict
def student_total(students,name):
    total = sum(students[name])
    print("arun total mark:",name,",",total)

students = {
    "arun_01":[90,95,88,92,100],
    "vijay_02":[100,65,88,90,100],
    "madhan_03":[90,95,88,92,85],
    "madhan_04":[100,65,88,90,100]
}
student_total(students,"arun_01")

subjects = ["tamil","english","maths","chemistry","physics"]

# percentage
def calculate_percentage(students, name):
    total = sum(students[name])
    percentage = total / len(students[name])
    print( "Percentage:",name, percentage)
calculate_percentage(students,"arun_01")

# pass or fail
def check_pass_fail(students, name):
    if min(students[name]) >= 35:
        print(name, "Result: Pass")
    else:
        print(name, "Result: Fail")

check_pass_fail(students,"arun_01")

# grade
def calculate_grade(students, name):
    total = sum(students[name])
    percentage = total / len(students[name])

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    print(name, "Grade:", grade)

calculate_grade(students,"arun_01")


# find_centum
def find_centum_subject(students, name, subjects):
    marks = students[name]
    for i in range(len(marks)):
        if marks[i] == 100:
            print(name, "Centum in", subjects[i])

find_centum_subject(students,"arun_01",subjects)

# cutoff
def calculate_cutoff(students, name):
    marks = students[name]
    cutoff = marks[2] + marks[3] + marks[4]
    print(name, "Cutoff:", cutoff)

calculate_cutoff(students,"arun_01",)

# top score 
def find_top_score(students):
    top_score = 0
    for marks in students.values():
        highest_mark = max(marks)

        if highest_mark > top_score:
            top_score = highest_mark
    print("top score:",top_score)

find_top_score(students)
        # marks = studen
# for names,marks in students.items():



# arun_total = sum(students["arun_01"])
# print("Arun total mark:",arun_total)


# print(students)
# subjects = ("tamil","english","maths","science","social")

# total = tamil + english + maths + sciencs + social
# print("Total marks:",total)

# for names,marks in students.items():
#    total= sum(marks)

# def student_results(name,marks):
    #  total = sum(marks)
    #  print("student name:",name)
    #  print("student marks:",marks)
    # #  print("total:",total)
    # print("hello")

