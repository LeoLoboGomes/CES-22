file1 = open("alice.txt", "r")
file2 = open("alice_words.txt", "w")
content = file1.read()
words = content.split()
words_counts = {}
for word in words:
    words_counts[word] = words_counts.get(word, 0) + 1
word_items = list(words_counts.items())
word_items.sort()
file2.write("Word              Count\n")
file2.write("=======================\n")
for (word, number) in word_items:
    string = "{0:<18}{1}".format(word, str(number))
    file2.write(string + "\n")
file1.close()
file2.close()
