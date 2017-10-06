import requests
import re
import sys
import threading

def getTitle(url):
        try:
                _ = re.search('<title>(.*?)</title>', requests.get(url,timeout=20).content)
                print url, _.group(1)+'\n'
        except:
                pass

def readText(txtpath):
        libs = []
        fp = open(txtpath,'r')
        while 1:
                line = fp.readline()
                if line:
                        libs.append(line.strip())
                else:
                        break
        fp.close()
        return libs

if __name__ == '__main__':
        urls = readText(sys.argv[1])
        for i in urls:
                th = threading.Thread(target = getTitle, args = (i,))
                th.start()
