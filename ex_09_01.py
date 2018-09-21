file_name = input('Enter a fie name:')
file_handle = open(file_name)
days = list()
days_count = dict()
for line in file_handle:
    if line.startswith('From '):
        line = line.strip()
        words = line.split()
        days.append(words[2])
for day in days:
    days_count[day] = days_count.get(day, 0) + 1
print(days_count)
