from numpy import *
import cv2 as cv

# Open image file using OpenCV
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
filename = "analise/Fig-0"
img = cv.imread(filename+".png")
img = cv.GaussianBlur(img, (5, 5), 0)
# img = cv.GaussianBlur(img, (5, 5), 0)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
height, width = img.shape

# img[ img>=200 ] = 255
# img[ img<200 ] = 0


num_pixels = height*width

with open(filename+".vtk",'w') as fid:

    # write header file
    fid.write("# vtk DataFile Version 2.0\n")
    fid.write("Cube example\n")
    fid.write("ASCII\n")
    fid.write("DATASET POLYDATA\n")

    num_points = (height+1)*(width+1)
    fid.write("POINTS %d float\n" % num_points)

    # colunas (width)  -> x
    # linhas  (height) -> y

    for y in range(height,-1,-1):
        for x in range(width+1):
            fid.write('%d %d 0\n' % (x, y))

    fid.write("POLYGONS %d %d\n" % (num_pixels, 5*num_pixels) )
    idx1 = 0
    idx2 = width+2
    for i in range(height):
        for j in range(width):
            fid.write('4 %d %d %d %d\n' % (idx1, idx1+1, idx2, idx2-1))
            idx1 = idx1 + 1
            idx2 = idx2 + 1
        idx1 = idx1 + 1
        idx2 = idx2 + 1

    fid.write('CELL_DATA %d\n' % (num_pixels))
    fid.write('SCALARS cell_scalars int 1\n')
    fid.write('LOOKUP_TABLE default\n')
    for i in range(height):
        for j in range(width):
            fid.write('%d\n' % img[i, j])