# def add(x, y):
#     print(x + y)

# add(5, 4)

# def sub(x, y):
#     print(x - y)
     
# sub(10,5)

# def mul(x, y):
#     print(x * y)

# mul(8,8)

# def div(x, y):
#     print(x / y)

# div(22,9)

# def floor_div (x , y):
#     print(x // y)

# floor_div(9,8)

# def can_vote(age):
#     print(age >= 18)

# can_vote(17)

# def is_minor(age):
#     print(age <= 18)

# is_minor(9)
# is_minor(25)

# def is_centum(mark):
#     print("is_centum", mark == 100)

# is_centum(100)

# def has_fever(temp):
#     print("has_fever",temp > 100.5)

# x = int(input("has_fever:"))
# has_fever(x)

# def add (a,b,c):
#     z = a+b+c
#     return z

# add(10,20,30)
 
def max (x , y):        # x = 10 ,y = 20 false
    z =  x > y      # result = false then y is big number
    if z == True:
        return x
    else:
        return y
    
result= max(20,10)
print(result) 

def min (a,b):
    if a < b:
        return a
    else:
        return b
    
result = min(20,10)
print(result)


# x is even -> x
# x is odd -> 2x

# x = 11
# if x % 2 ==0:
#     print (x)
# else:
#     print (2 * x)

# def even ():
#     x = 11
#     if x % 2 ==0:
#         print (x)
#     else:
#         print (2 * x)

# even()

# def even (x):
#     if x % 2 ==0:
#         print (x)
#     else:
#         print (2 * x)

# even(11)
# even(10)

def even (x):
    if x % 2 ==0:
        return (x)
    else:
        return (2 * x)

result = even(11)
print(result) 



