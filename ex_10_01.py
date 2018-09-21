emails_dict = dict()
emails_list = list()
while True:
    file_name = input('Enter a file name:')
    try:
        file_handle = open(file_name)
        break
    except:
        print('No such file')
for line in file_handle:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        emails_dict[words[1]] = emails_dict.get(words[1], 0) + 1
for key, value in list(emails_dict.items()):
    emails_list.append((value, key))
emails_list.sort(reverse=True)
for value, key in emails_list:
    print(key, value)
