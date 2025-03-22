
word = "bottles"

for i in range(99, 0, -1):
    if i == 1:
        word = "bottle"

    print(i,word, "of the beer on the wall,")
    print(i,word, "of the beer.")
    print("Take one down, pass it around,")
    if i == 1:
             print("No more bottles of beer on the wall!")
    else:
        if i == 2:
            word = "bottle"
        print(i-1 ,word, "of the beer on the wall.\n")