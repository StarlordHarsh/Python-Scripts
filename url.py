import urllib

url = urllib.urlopen("http://google.com/")

data = url.read()

print data 