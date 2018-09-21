file_name = input('Enter a file name:')
file_handle = open(file_name)
count = 0
for line in file_handle:
    line = line.strip()
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        email = words[1]
        print(email)
print('There were ' + str(count) +
      ' lines in the file with From as the first word')
