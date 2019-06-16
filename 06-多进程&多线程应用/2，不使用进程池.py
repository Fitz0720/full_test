# -*- coding: utf-8 -*-
import time, os
from multiprocessing import Pool, Process
import http_request


def run(fn):
    # fn: 函数参数是数据列表的一个元素
    # time.sleep(1)
    print("############:{}".format(os.getpid()))
    http_request.http(fn)
    # print(123456789123456789 * 123456789123456789 * 98765421 * fn)
    return "hhhh"


def func_bk(p):
    print("回调函数被调用：", p)


if __name__ == "__main__":
    testFL = [i for i in range(30)]
    print('shunxu:')  # 顺序执行(也就是串行执行，单进程)
    s = time.time()
    # for fn in testFL:
    #     run(fn)
    t1 = time.time()
    print("顺序执行时间：", t1 - s)

    print('concurrent:')  # 创建多个进程，并行执行
    p_list = []
    for i in testFL:
        p = Process(target=run, args=(i, ))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    t2 = time.time()
    print("并行执行时间：", t2 - t1)



"""
顺序执行时间： 6.039072751998901
concurrent:
并行执行时间： 1.3695518970489502

顺序执行时间： 6.02333402633667
并行执行时间： 1.3404762744903564
"""

