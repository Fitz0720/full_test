class ClassA(object):
    def __init__(self):
        print("classA实例成对象")

    def test(self):
        print('test')

    int_value = 1
    # str_value = __author__


# 全局方法，加载时会被调用
print(__file__, 'global function.')

if __name__ == '__main__':
    print(__file__, __name__)
