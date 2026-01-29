week_days = {"mon","tues","wed","thur","fri"}
week_end = {"sat","sun"}

all_days = week_days | week_end
print(all_days)

difference= all_days - week_end
print(difference)

intersect = all_days & week_days
print(intersect)

symmetric_difference = week_days ^ week_end
print(symmetric_difference)