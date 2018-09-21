import urllib.request
import re
count = 0
while True:
    url = input('URL--> ')
    if re.search('https?://.+', url):
        host = url.split('/')[2]
        break
    else:
        print('Invalid URL')
        continue
file = urllib.request.urlopen(url).read().decode()

#fhand = open('test.txt', 'wb')
# fhand.write(file_handle)
# fhand.close()
for word in file:
    #    char = char.decode()
    count = count + 1
    if count <= 3000:
        print(word, end='')
print('\nOverall number of characters:', count)
