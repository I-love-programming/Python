file_name = input('Enter a file name:')
file_handle = open(file_name)
count_lines = 0
total = 0
for line in file_handle:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.strip()
        count_lines = count_lines + 1
        count_letters = 0
        for letter in line:
            if letter == ' ':
                break
            else:
                count_letters = count_letters + 1
        number = float(line[count_letters + 1:len(line)])
        total = total + number
average = total / count_lines
print('Aveaverage spam confidence:', average)
