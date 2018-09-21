hour_counts = dict()
hour_list = list()
while True:
    file_name = input('Enter a file name:')
    try:
        file_handle = open(file_name)
        break
    except:
        print('No such file')
for line in file_handle:
    if line.startswith('From '):
        line = line.strip()
        words = line.split()
        words = words[5].split(':')
        hour_counts[words[0]] = hour_counts.get(words[0], 0) + 1
hour_list = list(hour_counts.items())
hour_list.sort()
for hour, count in hour_list:
    print(hour, count)
