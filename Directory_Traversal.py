import os
import os.path


def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".png")]


def dfs_show_dir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("| " * depth + "+--" + item)

            newitem = path + '/' + item
            if os.path.isdir(newitem):
                dfs_show_dir(newitem, depth + 1)


if __name__ == '__main__':
    dfs_show_dir('.', 0)
