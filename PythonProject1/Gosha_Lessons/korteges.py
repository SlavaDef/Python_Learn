# Кортеджі (tuple) це ті ж списки але константні в них не можна міняти данні, видаляти щось, додавати щось

elements = (3, 88 ,66.5, True, "Hello", (1, 2, 3), 88.1, [7, 8, 9])
print(elements)
print(elements[::5]) # step 5 print first and 5
print(elements[::2])
print(elements[2::]) # from second ind to end
print(elements[-1][0])  # 7 -1=last element

print(elements[2:-2:2]) # from second el to -2 el step 2

print(len(elements))
print(elements.count(88),'\n') # 1 because we have one element = 88

info = 66, 12, 87 # another way of creating tuple
print(info)

for el in elements:
    print(el)

i=0
while i<len(elements):
    print(elements[i])
    i+=1

nums = [1, 2, 3, 4, 5]

new_nums = tuple(nums) # there we tuple from massive
print(new_nums)
