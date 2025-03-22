
word = True;

while word:
    user_input = input("Enter a word: ")
    if user_input == "quit":
        break
        #word=False
    print("Length of the word is: ", len(user_input), user_input)