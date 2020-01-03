import numpy as np
import cv2

print('opencv version:', cv2.__version__)

image_path = '/home/zexi/rubiks_cube/LINEMOD/rubikscube/JPEGImages/000001.jpg'
image = cv2.imread(image_path)
b, g, r = cv2.split(image)
row, col = b.shape[0], b.shape[1]
b_linear = (b.reshape(1, row*col)).astype(np.float64)
mean_b = np.mean(b_linear, axis=0)

mean, eigenvectors = cv2.PCACompute(b_linear, mean_b.reshape(1, -1))

points = cv2.PCAProject(b_linear, np.array(), None)

image_linear = image.reshape(1, image.shape[0]*image.shape[1])
image_linear = image_linear.astype(np.float64)

mean_b, _ = cv2.meanStdDev(b)

g_linear = g.reshape(1, row*col)
r_linear = r.reshape(1, row*col)


row, col = image.shape[0], image.shape[1]

b, g, r = cv2.split(image)

mean_g, _ = cv2.meanStdDev(g)
mean_r, _ = cv2.meanStdDev(r)

pca_mean_b, eigenvectors_b = cv2.PCACompute(b, mean_b[0][0])
pca_mean_g, eigenvectors_g = cv2.PCACompute(g, mean_g[0][0])
pca_mean_r, eigenvectors_r = cv2.PCACompute(r, mean_r[0][0])



# mean, std_dev = cv2.meanStdDev(image)

# print('mean: ', mean)
# print('std_dev: ', std_dev)

import numpy as np
# mean, eigenvectors = cv2.PCACompute(image, mean)

# np_mean = np.mean(image)
# print('np_mean: ', np_mean)