while True:
    try:
        file_name = input('please enter a file name:')
        file_handle = open(file_name)
        break
    except:
        print('No such file:', file_name)
        continue
count = 0
for line in file_handle:
    count = count + 1
    if count < 6:
        line = line.upper()
        print(line[:len(line) - 1])
