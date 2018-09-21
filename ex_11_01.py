import re
reg = input('Enter a regular expression: ')
file_handle = open('mbox.txt')
count = 0
for line in file_handle:
    if re.search(reg, line):
        count = count + 1
print('mbox.txt had ' + str(count) + ' lines that matched ' + reg)
