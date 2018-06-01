from skimage.io import imread, imsave, imshow, show

img = imread("img.png")
nose = img[370:410, 350:440]
# imshow(nose)
# show()
img[370:410, 350:440] = [255, 0, 255]
imshow(img)
show()