import os
import os.path


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
