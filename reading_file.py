file_handle = open('mbox-short.txt')
count = 0
for line in file_handle:
    count = count + 1
    if count < 10:
        print(line[:len(line) - 1])
print('Line Count:', count)
