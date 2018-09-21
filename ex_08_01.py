file_name = input('Enter file:')
file_handle = open(file_name)
words_collection = list()
for line in file_handle:
    words = line.split()
    for word in words:
        if word not in words_collection:
            words_collection.append(word)
words_collection.sort()
print(words_collection)
