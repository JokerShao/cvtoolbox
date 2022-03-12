import os
import io
import hashlib


# 1st is the base folder, if you want work in 1 folder, let other empty
target_path_list = [
    'corner', # 要留存相同文件的文件夹
    'corner', # 准备删除、清空的文件夹
]

def compute_md5(fname, blk_size=1024*8):
    m = hashlib.md5()
    file = io.FileIO(fname, 'rb')
    bytes = file.read(blk_size)
    while (bytes != b''):
        m.update(bytes)
        bytes = file.read(blk_size)
    file.close()
    return m.hexdigest()

md5_fname_dict = dict()

for target_path in target_path_list:
    for root, dirs, files in os.walk(target_path, topdown=False):
        for fname in files:
            fullfilename = os.path.join(root, fname)

            md5_value = compute_md5(fullfilename)
            if md5_value in md5_fname_dict:
                print('find same md5: {} => {}'.format(md5_fname_dict[md5_value], fullfilename))
                # os.remove(fullfilename)
            else:
                md5_fname_dict[md5_value] = fullfilename
                print(len(md5_fname_dict))

