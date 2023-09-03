from numpy import *


import cv2 as cv


filename = "Fig3a-cut"
img = cv.imread(filename+".jpg")
img = cv.GaussianBlur(img, (5, 5), 0)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
npxh, npxv = img.shape


# npxh, npxv = (2, 4)
# img = zeros((npxh, npxv))

f = open(filename+".vtk",'w')
f.write('# vtk DataFile Version 2.0\n'
        'Cube example\n'
        'ASCII\n'
        'DATASET UNSTRUCTURED_GRID\n')
f.write('POINTS %d float\n' % ((npxh+1)*(npxv+1)))
for i in range(npxh+1):
    for j in range(npxv+1):
        f.write('%d %d 0\n' % (i, j))
f.write('CELLS %d %d\n' % (npxv*npxh, 5*npxv*npxh ))

idx1 = 0
idx2 = npxv+2
for i in range(npxh):
    for j in range(npxv):
        f.write('4 %d %d %d %d\n' % (idx1, idx1+1, idx2, idx2-1))
        idx1 = idx1 + 1
        idx2 = idx2 + 1
    idx1 = idx1 + 1
    idx2 = idx2 + 1

f.write('CELL_TYPES %d\n' % (npxv*npxh))
for i in range(npxv*npxh):
    f.write('9\n')

f.write('CELL_DATA %d\n'% (npxh*npxv))
f.write('SCALARS cell_scalars int 1\n')
f.write('LOOKUP_TABLE default\n')

for i in range(npxv):
    for j in range(npxh):
        f.write('%d\n' % img[j, i])


f.close()
