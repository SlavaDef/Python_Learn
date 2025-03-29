import time

time_now = time.time()
print(time.ctime(time_now))

# Метод time.localtime() приймає часову мітку та повертає struct_time (кортеж, який містить 9 елементів)
# за локальним часом.
result = time.localtime(time_now) # the same, result = time.localtime() by defolt
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
