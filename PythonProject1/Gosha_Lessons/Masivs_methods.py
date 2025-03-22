nums = [33, 26, 16, 22, 158]
print(nums, "\n")

nums.reverse()
print(nums, "\n")

nums.sort()
print(nums, "\n")

objects = [66, 77.8, True, 'some text', 65.7, "enother text", [False, 22, "something"]]

print(objects, "\n")

print(objects[2], "\n")

print(objects[6][1], "\n") #

print(objects[-1][1], "\n") # -1 = last element in massiv

print("first з кінця = ", objects[-1], "\n") # -1 = last element in massiv

print("другий з кінця = ", objects[-2], "\n") # -2 = другий з кінця

print('len of the object = ', len(objects), "\n")

third = objects.copy() # use only copy not third = objects

third.append(666)

print(objects, "\n")

print(third, "\n")

print(objects.count(66), "\n") # 1 becouse in masiv one 66