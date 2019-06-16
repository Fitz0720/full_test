# python动态加载模块、类、函数
# 2016年04月15日 23:31:46 shijc_csdn 阅读数：14684
#  版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/shijichao2/article/details/51165576
# 动态加载模块：
# 方式1：系统函数__import__()
# 方式2：imp, importlib 模块
# 方式3：exec 函数
#
# 动态加载类和函数
# 首先，使用加载模块，使用内置函数提供的反射方法getattr()，依次按照层级获取模块->类\全局方法->类对象\类方法。
#
# test_import_module.py
#
# class ClassA:
#     def test(self):
#         print('test')
#
#     int_value = 1
#     str_value = __author__
#
# # 全局方法，加载时会被调用
# print(__file__, 'global function.')
#
# if __name__ == '__main__':
#     print(__file__, __name__)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# test_import_module.py
#
# # 注意：模块名不包括.py后缀
# imp_module = 'test_import_class'
# imp_class = 'ClassA'
#
# # 方式1：使用__import__()导入模块
# # 导入指定模块，导入时会执行全局方法。
# ip_module = __import__(imp_module)
# # dir()查看模块属性
# print(dir(ip_module))
#
# # 使用getattr()获取imp_module的类
# test_class = getattr(ip_module, imp_class)
# # 动态加载类test_class生成类对象
# cls_obj = test_class()
# # 查看对象属性
# print(dir(cls_obj))
# for attr in dir(cls_obj):
#     # 加载非__前缀的属性
#     if attr[0] != '_':
#         # 获取导入obj方法。
#         class_attr_obj = getattr(cls_obj, attr)
#
#         # 判断类属性是否为函数
#         if hasattr(class_attr_obj, '__call__'):
#             # 执行函数
#             class_attr_obj()
#         else:
#             # 输出类属性值
#             print(attr, ' type:', type(class_attr_obj), ' value:', class_attr_obj)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 输出结果
#
# D:/work/python\test_import_class.py global function.
# ['ClassA', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'int_value', 'str_value', 'test']
# int_value  type: <class 'int'>  value: 1
# str_value  type: <class 'str'>  value: abc
# test
# 1
# 2
# 3
# 4
# 5
# 6
# # 方式2：使用importlib
# # importlib相比__import__()，操作更简单、灵活，支持reload()
# import importlib
# ip_module = importlib.import_module('.', imp_module)
# ip_module_cls = getattr(ip_module, imp_class)
# cls_obj = ip_module_cls()
# if 'int_value' in dir(cls_obj):
#     print(cls_obj.int_value)
#     cls_obj.int_value = 10
#     print(cls_obj.int_value)
#
# # reload()重新加载，一般用于原模块有变化等特殊情况。
# # reload()之前该模块必须已经使用import导入模块。
# # 重新加载模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块，reload后还是用原来的内存地址。
# ip_module = importlib.reload(ip_module)
# print(getattr(ip_module, imp_class).int_value)
#
# # 循环多次加载相同文件，手动修改文件数据，发现重新加载后输出内容变更。
# from time import sleep
# # for i in range(30):
#     ip_module = importlib.reload(ip_module)
#     print(getattr(ip_module, imp_class).int_value)
#     sleep(3)