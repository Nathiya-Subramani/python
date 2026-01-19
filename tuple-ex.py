# t = (10,20,30)
# print(t)
# # unpacking
# a,b,c = t
# print(a,b,c)
# # packing

# c = c + 10
# t =(a, b, c)
# print(t)

# product , quantity , price , revenue
# pen,100,20,0
# buy and sale functions
print(dir(tuple)) 


product = ("Pen", 100, 20, 0)

def buy(item):
    name, qty, price, revenue = item   # unpacking
    revenue = qty * price
    return (name, qty, price, revenue) # packing
