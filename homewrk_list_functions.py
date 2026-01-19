# print(dir(list))
# append(),insert(),pop(),remove(),clear(),reverse(),copy(),sort(),extend()

# append()
foods = ["idly","dosa","poori"]

foods.append("masala")
print(foods)

# insert()
foods.insert(2,"roti")
print(foods)

desert = ["brownie","fudgecakes","rasamalai"]
# extend()
foods.extend(desert)
print(foods)

# sort
foods.sort()
print(foods)

# pop()
foods.pop()
print(foods)

# reverse
foods.reverse()
print(foods)

# remove
foods.remove("fudgecakes")
print(foods)

# copy
foods_copy = foods.copy()
print(foods_copy)

# clear 
foods.clear()
print(foods)