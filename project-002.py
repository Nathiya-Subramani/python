# get marks per for all 5 subjects
# calculate total
# calculate student grade 
# find top score
# find pass are fail
# find subject with centum score
# calculate percentage 
# calculate cutoff (maths,physics,chemistry)


# get  marks

# tamil = int(input("enter tamil mark:"))
# english = int(input("enter english mark:"))
# maths = int(input("enter maths mark:"))
# chemistry = int(input("enter chemistry mark:"))
# physics = int(input("enter physics mark:"))

tamil = 90
english = 90
maths = 99
chemistry = 96
physics = 100

# calaculate total

# total = tamil + english + maths + chemistry + physics
# print("Total marks:",total) 

def calculate_total(ta,en,ma,ch,ph):
    total = ta + en + ma + ch + ph
    return total  

total = calculate_total(tamil,english,maths,chemistry,physics)
print("total marks:",total)

# calculate percentage

percentage = total / 500 * 100
print("percentage of a student:",percentage)

# pass or fail

if tamil >= 35 and english >= 35 and maths >= 35 and chemistry >= 35 and physics >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")

# check grade 

if percentage >= 90:
    print("grade:A")
elif percentage >= 75:
    print("grade:b")
elif percentage >= 60:
    print("grade:c")

else:
    print("grade:d")

# top score

top_score = max(tamil,english,maths,chemistry,physics)
print("Top score of a student:",top_score)

# check centum

if tamil == 100 or english == 100 or maths == 100 or chemistry == 100 or physics == 100:
    print("centum scored subject")
else:
    print("no centum scored")

#calculate cutoff

cutoff_marks = maths + (chemistry/2) +(physics/2)
print("cutoff (M+C+p):",cutoff_marks) 

#h/w
# convert all into function
# how many centums in (numbers)
# find top score subject