from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# show original picture
loc_input_img = os.path.join('..', 'DATA', 'INPUT', 'KIP.jpg')
np_image = np.array(Image.open(loc_input_img))
plt.imshow(np_image)
plt.show()

# show original picture 8 by 3
np_image2 = np.concatenate((np_image, np_image, np_image,
                            np_image, np_image, np_image, np_image, np_image), axis=1)
np_image3 = np.vstack((np_image2, np_image2, np_image2))
plt.imshow(np_image3)
plt.show()

# show mirrored pictures 
np_mirror1 = np.fliplr(np_image)
np_mirror2 = np.flipud(np_image)
np_mirror3 = np.fliplr(np_mirror2)
np_rij1 = np.concatenate((np_image, np_image, np_image, np_image, np_image, np_image), axis=1)
np_rij2 = np.concatenate((np_mirror1, np_mirror1, np_mirror1, np_mirror1, np_mirror1, np_mirror1), axis=1)
np_rij3 = np.concatenate((np_mirror2, np_mirror2, np_mirror2, np_mirror2, np_mirror2, np_mirror2), axis=1)
np_rij4 = np.concatenate((np_mirror3, np_mirror3, np_mirror3, np_mirror3, np_mirror3, np_mirror3), axis=1)
np_image3 = np.concatenate((np_rij1, np_rij2, np_rij3, np_rij4), axis=0)
plt.imshow(np_image3)
plt.show()

# show colored pictures
np_image_red = np_image.copy()
np_image_blue = np_image.copy()
np_image_green = np_image.copy()
np_image_red[:, :, [1,2]] = 0
np_image_green[:, :, [0,2]] = 0
np_image_blue[:, :, [0,1]] = 0
np_rij_red = np.concatenate((np_image_red, np_image_red, np_image_red, np_image_red), axis=1)
np_rij_green = np.concatenate((np_image_green, np_image_green, np_image_green, np_image_green), axis=1)
np_rij_blue = np.concatenate((np_image_blue, np_image_blue, np_image_blue, np_image_blue), axis=1)
np_image_colors = np.concatenate((np_rij_blue, np_rij_red, np_rij_red, np_rij_green),axis=0)
plt.imshow(np_image_colors)
plt.show()

# make original picture twice as big
np_double_img = np.repeat(np.repeat(np_image, 2, axis=0), 2, axis=1)
plt.imshow(np_double_img)
plt.show()

# make copy of np_double_img, we gonna need it later
np_copy_double_img =np_double_img.copy()

# merge colored pictures & big picture
for x in range(0,566,1):
    for y in range(0,566,1):
        np_image_colors[x + 283, y + 283] = np_double_img[x,y]
plt.imshow(np_image_colors)
plt.show()

# vertical striped picture
np_double_img = np_double_img[:-8, :-8]
for x in range(0, 541, 18):
    print(x)
    for y in range(0,6,1):
        np_double_img[:, x+y, [1, 2]] = 0
    for y in range(6, 13, 1):
        np_double_img[:, x + y, [0, 1]] = 0
    for y in range(13, 18, 1):
        np_double_img[:, x + y, [0, 2]] = 0

plt.imshow(np_double_img)
plt.show()

# checked picture 
np_double_img = np_copy_double_img.copy()
np_double_img = np_double_img[:-8, :-8]
for x in range(0, 558, 1):
    for y in range(0, 558, 1):
        if x <= 186 and y <= 186:
            np_double_img[x,y,[1,2]] = 0
        if 187 <= x <= 372 and y <= 186:
            np_double_img[x,y,[0,1]] = 0
        if 373 <= x <= 558 and y <= 186:
            np_double_img[x,y,[0,2]] = 0
        if x <= 186 and 187 <= y <= 372:
            np_double_img[x,y,[0,2]] = 0
        if 187 <= x <= 372 and 187 <= y <= 372:
            np_double_img[x,y,[1,2]] = 0
        if 373 <= x <= 558 and 187 <= y <= 372:
            np_double_img[x,y,[0,1]] = 0
        if x <= 186 and 373 <= y <= 558:
            np_double_img[x, y, [0, 1]] = 0
        if 187 <= x <= 372 and 373 <= y <= 558:
            np_double_img[x, y, [0, 2]] = 0
        if 373 <= x <= 558 and 373 <= y <= 558:
            np_double_img[x, y, [1, 2]] = 0
plt.imshow(np_double_img)
plt.show()
