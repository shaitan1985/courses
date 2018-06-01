from skimage.io import imread, imsave, imshow, show
from skimage import img_as_float, img_as_ubyte
import numpy

img = imread("img.png")

img_f = img_as_float(img)
r = img_f[:, :, 0]
g = img_f[:, :, 1]
b = img_f[:, :, 2]

img_combined = numpy.dstack((b, r, g))
imsave("out_img.png", img_as_ubyte(r*0.2126 + g*0.7152 + b*0.0722 ))
# avg_grey = (r + g + b) / 3



# imshow(avg_grey)
# show()

















# img = imread("img.png")
# shape = img.shape
# # print(shape)
# color = img[0, 0]
#
# tmp = [range(shape[1]), range(shape[1]-1,0,-1)]
# lst = []
# for x in range(2):
#     flag = True
#     counter = (shape[0]-1) * x
#     while flag:
#         for item in tmp[x]:
#             # print(item)
#             # print(counter, item)
#             if not numpy.array_equal(img[counter, item], color):
#                 lst.append(item)
#                 lst.append(counter)
#                 flag = False
#                 break
#
#         counter += (1 - (x*2))
# lst[2] = shape[1] - lst[2] - 1
# lst[3] = shape[0] - lst[3] - 1
# print("{} {} {} {}".format(lst[0], lst[1], lst[2], lst[3]))


# vert_start = int(shape[0]/ 2) - int(7 / 2)
# hor_start = int(shape[1]/ 2) - int(15 / 2)
# img[vert_start:vert_start+7, hor_start:hor_start+15] = [255, 192, 203]

# img_pink = imread("tiger-pink.png")
#
# print(numpy.array_equal(img, img_pink))
# for vert_item in range(shape[0]):
#     for hor_item in range(shape[1]):
#         first = img[vert_item, hor_item]
#         second = img_pink[vert_item, hor_item]
#         for item in range(3):
#             if first[item] != second[item]:
#                 # print(first[item] == second[item])
#                 print("{}:{} not equal: {}:{}".format(vert_item, hor_item, img[vert_item, hor_item],
#                                                       img_pink[vert_item, hor_item] ))

# imsave("out_img.png", img)

# imshow(img)
# show()