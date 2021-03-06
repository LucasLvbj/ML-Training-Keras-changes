# This does a convolution on an image
# if you get an error
# ImportError: No module named skimage
# you may need to run:
# > pip install scikit-image
# > pip install scipy

import numpy as np

from skimage import io
from skimage import data
from scipy.signal import convolve2d

image = io.imread(r'C:\Users\blv\PycharmProjects\ML-Training-Keras-changes\keras-cnn\dog.jpg', as_grey=True)

kernel = [[0.0, 0.0, 0.0],
          [10.0, 0.0, -10.0],
          [0.0, 0.0, 0.0]]

new_image = convolve2d(image, kernel)
new_image = new_image.clip(0.0, 1.0)

io.imsave(r'C:\Users\blv\PycharmProjects\ML-Training-Keras-changes\keras-cnn\out.png', new_image)
