import requests


def http(page_num):
    url = "http://book.zongheng.com/store/c1/c0/b0/u0/p{}/v9/s9/t0/u0/i1/ALL.html".format(page_num)
    res = requests.get(url=url, timeout=2).content
    print(res)


if __name__ == '__main__':
    url = "http://book.zongheng.com/store/c1/c0/b0/u0/p4/v9/s9/t0/u0/i1/ALL.html"
    http(url)
