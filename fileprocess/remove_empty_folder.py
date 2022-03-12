import os

target_path = '.'

macos_store = '.DS_Store'


for root, dirs, files in os.walk(target_path, topdown=False):
    # root: current absolute path
    # dirs: all sub directory in current path
    # files: all file in current path

    # if is empty, rmdir
    if not files and not dirs:
        print('rmdir:', root)
        os.removedirs(root)

    # only a ".DS_Store" file, rm this file and rmdir
    elif not dirs and len(files)==1:
        if files[0]==macos_store:
            print('rm:', os.path.join(root, macos_store))
            os.remove(os.path.join(root, macos_store))
            print('rmdir:', root)
            os.removedirs(root)

