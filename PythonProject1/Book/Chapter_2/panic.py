phrase = "Don't panic!"
plist = list(phrase)
print(plist)
print(phrase)

list1 = ["o","n","t","p"]
list_new=[]


for char in plist:
    if char in list1:
        if char not in list_new:
            list_new.append(char)
list_new.insert(2," ")
list_new.insert(4, "a")


new_phrase = "".join(list_new)
print(new_phrase)