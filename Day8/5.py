sentence = input("Enter the sentence: ")
search_word = input("Enter the word: ")
count = 0

words = sentence.split()
for word in words:
    if word == search_word:
        count +=1

print(f"The total number of occurrence of {search_word} in sentence is {count}")
