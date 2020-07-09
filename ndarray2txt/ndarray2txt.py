import numpy as np

K1 = np.ones((3,3), dtype=np.float64)
K2 = np.ones((3,3), dtype=np.float64)
K3 = np.ones((3,3), dtype=np.float64)
K4 = np.ones((3,3), dtype=np.float64)

K = [K1, K2, K3, K4]

D1 = np.zeros((1, 5), dtype=np.float64)
D2 = np.zeros((1, 5), dtype=np.float64)
D3 = np.zeros((1, 5), dtype=np.float64)
D4 = np.zeros((1, 5), dtype=np.float64)

D = [D1, D2, D3, D4]


f_fc = open('fc.txt', 'w')
f_kc = open('kc.txt', 'w')
f_cc = open('cc.txt', 'w')


for i in range(4):
    f_fc.write(str(K[i][0, 0])+' '+str(K[i][1,1])+'\n')
    f_kc.write(str(K[i][0, 2])+' '+str(K[i][1, 2])+'\n')
    f_cc.write(str(D[i][0, 0])+' '+ \
                str(D[i][0, 1])+' '+ \
                str(D[i][0, 2])+' '+ \
                str(D[i][0, 3])+' '+ \
                str(D[i][0, 4])+'\n')

f_fc.close()
f_kc.close()
f_cc.close()
