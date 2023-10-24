# library numpy -> pip install numpy
# library imageio -> pip install imageio
# library scipy -> pip install scipy
# library opencv -> pip install opencv-python
# kita pakai library image yang kemarin (pip iinstall image)
# siapkan 1 gambar di folder yang sama untuk diconvert

# import library yang akan digunakan
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "build.jpg" # nama file input

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    #formula untuk convert img -> grayscale // pakai kode warna matlab

def dodge(front,back):
    final_sketch = front*255/(255-back)
    # kalau gambarnya lebih besar dari 255 bit/px maka akan diconvert jadi 255
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255

    return final_sketch.astype('uint8')

ss = imageio.imread(img) # untuk read gambar yang dipilih diawal tadi
gray = rgb2gray(ss) # untuk convert gambar jadi black and white

i = 255-gray

# untuk memberi efek blur
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
# sigma=15 adalah intensitas blurnya

r = dodge(blur,gray)
# untuk convert gambarnya (dengan memaplikasikan blur & black&white tadi)

cv2.imwrite("sketsa.png", r) # untuk menghasilkan output gambar
# run > start debugging