import urllib.request
import os

def getURLFileSize(url):
    request = urllib.request.Request(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'})
    request.get_method = lambda : 'HEAD'

    f = urllib.request.urlopen(request)
    print(f.headers)

    if "Content-Length" in f.headers:
        size = int (f.headers["Content-Length"])
    else:
        size = len (f.read ())
    return size

def tranverseFileSize():
    dirpath = 'xxxxxxx'
    oszlist = os.listdir(dirpath)
    for file in oszlist:
        print(os.path.getsize(dirpath + '\\' + file))

# ===== file reading/ writing & regular expression =====
file = open("reader.txt")
wfile = open("writer.txt", 'w')

while 1:
    line = file.readline()
    if not line:
        break
    
    match = re.search('[0-9]*', line)
    if match:
        wfile.write(match.group() + '\n')
    else:
        wfile.write(line)