import re
count = 0
total = 0
while True:
    file_name = input('Enter a file name: ')
    try:
        file_handle = open(file_name)
        break
    except:
        print('No such file!')
        continue
for line in file_handle:
    if re.search('New Revision: [0-9]+', line):
        temp = re.findall('New Revision: ([0-9]+)', line)
        total = total + int(temp[0])
        count = count + 1
print(total / count)
