phrase = "Don't panic!"
plist = list(phrase)
print(plist)
print(phrase)

newList = plist[1:8]
newList[2] = " "
newList.insert(4,newList.pop())
newList.pop(5)
#print(newList)

new_phrase = "".join(newList)
print(new_phrase)