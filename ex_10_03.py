words = dict()
words_list = list()
sum = 0
while True:
    file_name = input('Enter a file name:')
    try:
        file_handle = open(file_name)
        break
    except:
        print('No such file')
for line in file_handle:
    for word in line:
        if word.isalpha():
            word.lower()
            words[word] = words.get(word, 0) + 1
for word, count in list(words.items()):
    words_list.append((count, word))
    sum = sum + count
words_list.sort(reverse=True)
for count, word in words_list:
    print(word, count, '{:.3%}'.format(count / sum))
