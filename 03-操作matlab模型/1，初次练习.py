import scipy.io

home = scipy.io.loadmat('./mat/home.mat')
no_home = scipy.io.loadmat('./mat/nohome.mat')
hbuild = scipy.io.loadmat('./mat/highbuild.mat')

# data类型为dictionary
print(home.keys()) # 即可知道Mat文件中存在数据名，假设存在'x', 'y'两列数据
print(no_home.keys()) # 即可知道Mat文件中存在数据名，假设存在'x', 'y'两列数据
print(hbuild.keys()) # 即可知道Mat文件中存在数据名，假设存在'x', 'y'两列数据

"""
dict_keys(['__header__', '__version__', '__globals__', 'net'])
dict_keys(['__header__', '__version__', '__globals__', 'netfeizhuzhai'])
dict_keys(['__header__', '__version__', '__globals__', 'net'])
"""

home_net = home["net"]
nohome_netfeizhuzhai = no_home["netfeizhuzhai"]
hbuild_net = hbuild["net"]

print(home_net)
print("="*102)
print(nohome_netfeizhuzhai)
print("="*102)
print(hbuild_net)

# print(data['x'])
# print(data['y'])