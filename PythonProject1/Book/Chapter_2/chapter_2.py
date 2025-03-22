nums = [66,88,77,99]
print(nums)
nums.remove(77) # remove delete element by his
print(nums,"\n")

nums2 = [23.6,44.5,22.8,66.3,12.8]
print(nums2)
print(nums2.pop(2)) # pop delete and return element by index
print(nums2,"\n")

print(nums)
nums.extend([15,25,35]) # add enother list in the end of list
print(nums,"\n")

print(nums2)
nums2.insert(0,11.1) # add in the begining of list by index
nums2.insert(2,"so-so") # by index
print(nums2,"\n")