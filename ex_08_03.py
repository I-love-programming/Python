num_list = list()
while True:
    number = input('Enter a number:')
    if number == 'done':
        break
    else:
        number = int(number)
        num_list.append(number)
maximum = max(num_list)
minimum = min(num_list)
print('Maximum: ', maximum)
print('Minimum: ', minimum)
