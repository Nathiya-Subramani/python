# fruit = " fruit is a very healthy one "

# upper,lower,caps,split,join,find,start with,end with

# up = fruit.upper()
# print("upper:",up)

# low = fruit.lower()
# print("lower:",low)

# caps = fruit.title()
# print("title:",caps)

# split = fruit.split()     
# print("split:",split)

# start = fruit.startswith(" fruit")
# print("Start ?:", start)

# end = fruit.endswith("one ")
# print("End ?:", end)

# pos = fruit.find("healthy")
# print("Position :", pos)

# join = " ".join(split)
# print("join:",join)

name = "nathiya"
age = 20
gender = "female"

greeting_template = "hello {0} , your age is {1}, your gender is {2}".format(name,age,gender)
print(greeting_template)


greeting_template = "hello {0} , your age is {1}, your gender is {2}"
greeting = greeting_template.format(name,age,gender)
print(greeting)

