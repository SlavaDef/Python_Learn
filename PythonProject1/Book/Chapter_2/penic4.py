phrase = "Don't panic!"
plist = list(phrase)
print(plist)
print(phrase)

newList = "".join(plist[1:3]) # join first 3 lettrs in massive # on
#newList.append(plist[5])
#newList.append(plist[4])
#newList.append(plist[7])
#newList.append(plist[6])

#newList.append("".join([plist[5], plist[4], plist[7], plist[6]]))

newList = newList + "".join([plist[5], plist[4], plist[7], plist[6]]) # on + 4 letters = on tap

#print("".join(newList))

print(newList) # on tap