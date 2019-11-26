import os
'''设置工作默认目录，使数据保持统一的存放格式，方便管理，若路径不存在将创建相应的目录及其结构'''
data_name = "shilintong2"


def copy_dirs(source, dist):
    """
    复制source下所有目录到dist目录中，若dist不存在将创建
    :param source: string
        源目录
    :param dist: string
        目标目录
    :return: nothing
    """
    if not os.path.exists(dist):
        os.makedirs(dist)
        children = os.listdir(source)
    for child_dir in children:
        next_source = os.path.join(source, child_dir)
        if os.path.isdir(next_source):
            next_dist = os.path.join(dist, child_dir)
            copy_dirs(next_source, next_dist)


base_dir = ".\\format_dir\\"
full_path = base_dir+data_name
model_path = base_dir+"example"
if not os.path.exists(full_path):
    copy_dirs(model_path, full_path)
os.chdir(full_path)   # 改变当前路径到设置的data_name文件夹下
print(os.getcwd())
