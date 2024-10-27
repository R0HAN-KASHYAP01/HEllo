sentence = input("Enter the sentence: ")
change = input("Enter the word to be changed: ")
new = input("Enter the new word: ")


after_replace = ""
words = sentence.split()

for word in words:
    if word == change:
        after_replace += new+ " "
    else:
        after_replace += word + " "

print(f"The sentence after replacing the words is:-\n{after_replace}")

