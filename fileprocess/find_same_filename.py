import os


target_path = '.'

# check same filenames file
filename_dict = dict()

for root, dirs, files in os.walk(target_path, topdown=False):
    for fname in files:
        fullfilename = os.path.join(root, fname)

        if fname in filename_dict:
            print('find same filename: {} => {}'.format(filename_dict[fname], fullfilename))
            # os.remove(fullfilename)
        else:
            filename_dict[fname] = fullfilename
            # print("'{}' add to dict".format(fname))

