from multiprocessing.dummy import Pool as ThreadPool
import requests
import sys
from bs4 import BeautifulSoup

def check(url):
    try:
        f = len(BeautifulSoup(requests.get('http://{}/jdaoisjdoaijsdoiajsd.php'.format(url),timeout=5).text,"html.parser").find_all())
        r = len(BeautifulSoup(requests.get('http://{}/admin.php'.format(url),timeout=5).text,"html.parser").find_all())
        if r != f:
            return url
    except:
        pass


if __name__ == '__main__':
    f = open(sys.argv[1]).read().split("\n")
    pool = ThreadPool(processes=200)
    return_list = pool.map(check, f)
    pool.close()
    pool.join()
    w = open('/tmp/out.txt','w')
    ret = [x for x in return_list if x not in ['', ' ', None]]
    for i in ret:
        w.write(str(i)+'\n')
    w.close()
