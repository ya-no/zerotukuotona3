#coding:utf-8

# 画像のconvolution（畳みこみ処理）のサンプル

from PIL import Image
import numpy as np
from scipy import signal

# 画像の読み込み
im = np.array(Image.open('lenna.png'))
print(im.ndim, im.shape) # 次元数、サイズ

# 3x3平均化
filter3x3 = [ [1,1,1],
              [1,1,1],
              [1,1,1],]
filter3x3 = np.array(filter3x3)
filter3x3 = filter3x3 / 9.0

imout = signal.convolve2d(im[:,:,1], filter3x3, 'same')
Image.fromarray(imout).convert('RGB').save('filter3x3.jpg')

# 5x5平均化
filter5x5 = [ [1,1,1,1,1],
              [1,1,1,1,1],
              [1,1,1,1,1],
              [1,1,1,1,1],
              [1,1,1,1,1],]
filter5x5 = np.array(filter5x5)
filter5x5 = filter5x5 / 25.0

imout = signal.convolve2d(im[:,:,1], filter5x5, 'same')
Image.fromarray(imout).convert('RGB').save('filter5x5.jpg')

# 水平方向微分
filter_dH = [ [ 0, 0, 0],
              [ 0, 1,-1],
              [ 0, 0, 0],]
filter_dH = np.array(filter_dH)
filter_dH = filter_dH / 1.0

imout = signal.convolve2d(im[:,:,1], filter_dH, 'same')
Image.fromarray(np.absolute(imout)).convert('RGB').save('filter_bibunH.jpg')

# 垂直方向微分

