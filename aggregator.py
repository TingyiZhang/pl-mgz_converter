import os
import numpy as np
from skimage.io import imread, imsave

# Stack all labels
out_dir = './whole/'

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

path = './out/masks/100307/'
labels = os.listdir(path)

for n in range(90, 100):
    img = np.zeros((256, 256), dtype=np.uint8)
    for label in labels:
        if not os.path.isdir(path + label):
            continue
        mask = imread(path + label + '/i_z' + "{:0>3}".format(str(n + 1)) + '.png')
        for i in range(256):
            for j in range(256):
                if mask[i, j] != 0:
                    img[i, j] = mask[i, j]

    print(out_dir + 'whole' + str(n) + '.png')
    imsave(out_dir + 'whole' + str(n) + '.png', img)

