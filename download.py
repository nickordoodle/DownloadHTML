import urllib.request

fid = urllib.request.urlopen('http://www.nickscherer.io/')
html = fid.read().decode('utf-8')

print(html)
