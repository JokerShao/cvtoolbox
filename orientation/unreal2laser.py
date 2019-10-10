import sys
import csv
import numpy as np
import rotationtools as rt


def unreal2laser(raw):
    """ doc string """
    x, y, z, qw, qx, qy, qz = raw
    return np.array([-y/100, z/100, x/100, qw, qy, -qz, -qx])

def read_csv(filename):
    """ doc string """
    # 读取csv至字典
    csvFile = open(filename, "r")
    reader = csv.reader(csvFile)

    # 建立空字典
    result = list()#{}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        result.append(item[2:9])
    csvFile.close()
    return np.array(result).astype(np.float64)

if __name__ == "__main__":
    #filename = 'cam_Memory_20190507181023.csv'
    filename = str(sys.argv[1])
    rawdata = read_csv(filename)

    eulerlist = list()

    for line in rawdata:
        ans = unreal2laser(line)
        T, Q = ans[:3], ans[3:]
        euler = rt.quat2euler(Q)
        eulerlist.append(np.hstack([T, euler]))

    eulerarray = np.array(eulerlist)
    np.savetxt('./eulerangle.csv', eulerarray, delimiter=',')

