# -*- coding: utf-8 -*-
import time, os
from multiprocessing import Pool, Queue
import http_request


def run(fn):
    # fn: 函数参数是数据列表的一个元素
    # time.sleep(1)
    print("############:{}".format(os.getpid()))
    http_request.http(fn)
    # print(123456789123456789 * 123456789123456789 * 98765421 * fn)
    # return "hhhh"


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
    pool = Pool(4)  # 创建拥有10个进程数量的进程池
    # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
    # pool.map(run, testFL)
    # pool.map_async(run, testFL, callback=func_bk)
    pool.map_async(run, testFL)
    # pool.apply(run, args=(3, ))
    # pool.apply_async(run, testFL, callback=func_bk)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出
    t2 = time.time()
    print("并行执行时间：", t2 - t1)

"""
并行执行时间： 3.7414968013763428
"""