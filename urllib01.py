import urllib.request
#import urllib.parse
#import urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg').read()
fhand = open('cover.jpg', 'wb')
fhand.write(img)
fhand.close()
