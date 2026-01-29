# get marks per for all 5 subjects
# calculate total
# calculate student grade 
# find top score
# find pass are fail
# find subject with centum score
# calculate percentage 
# calculate cutoff (maths,physics,chemistry)

# get marks

tamil = 45
english = 30
maths = 35
chemistry = 96
physics = 100

# calaculate total

def calculate_total(ta,en,ma,ch,ph):
    total = ta + en + ma + ch + ph
    return total  

total = calculate_total(tamil,english,maths,chemistry,physics)
print("total marks:",total)

# calculate percentage

def calculate_percentage(total):
        return(total/500)*100
percentage = calculate_percentage(total)
print("percentage:",percentage)

# pass or fail

def pass_or_fail(ta,en,ma,ch,ph):
    if tamil >= 35 and english >= 35 and maths >= 35 and chemistry >= 35 and physics >= 35:
        return "PASS"
    else:
        return "FAIL"
    
result = pass_or_fail(tamil,english,maths,chemistry,physics)
print("pass_or_fail:",result)

# check grade 

def calculate_grade(percentage):
     if percentage >= 90:
          return "a"
     elif percentage >= 75:
          return "b"
     elif percentage >= 60:
          return "c"
     else:
          return "d"
     
grade = calculate_grade(percentage)
print("grade of a student:",grade)
     
# top score

def top_score(ta,en,ma,ch,ph):
     return max (ta, en , ma , ch, ph)

top = top_score(tamil,english,maths,chemistry,physics)
print("top score f a student:",top)

# check centum
def check_centum(ta,en,ma,ch,ph):
     if tamil == 100:
          print ("tamil centum")
     if english == 100:
          print ("english centum")
     if maths == 100:
          print ("maths centum")
     if chemistry == 100:
          print ("chemistry centum")
     if physics == 100:
          print ("physics centum")
          
check_centum(tamil,english,maths,chemistry,physics)

def check_mark(mark , subject):
     if mark == 100:
          print("centum in:",subject)

check_mark (tamil,"Tamil")
check_mark (100,"Maths")

#calculate cutoff 

def calculate_cutoff(ma, ph, ch):
    return ma + ph + ch

cutoff = calculate_cutoff(maths, physics, chemistry)
print("Cutoff:", cutoff)



#h/w
# convert all into function
# how many centums in (numbers)
# find top score subject