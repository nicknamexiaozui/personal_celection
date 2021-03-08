#-- coding: utf-8 --
#@Time : 2021/2/7 16:21
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : baidu_ai.py
#@Software: PyCharm
from wordcloud import WordCloud
import base64
import collections
import numpy as np
from PIL import Image
from aip import AipBodyAnalysis
import matplotlib.pyplot as plt
'''
百度云中已创建应用的  APP_ID API_KEY SECRET_KEY
代码在技术文档中有说明：https://cloud.baidu.com/doc/BODY/s/4k3cpyner
'''
APP_ID = '23631932'
API_KEY = 'z30mYxgOsBBFnPLcAWxEzw03'
SECRET_KEY = 'OayUz3McP92y34og62oQSyePdX1THgGg'
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
img='12.jpg'
with open(img, 'rb') as fp:
	img_info = fp.read()
seg_res = client.bodySeg(img_info)
#分割后的人像前景抠图，透明背景，Base64编码后的png格式图片，不用进行二次处理，直接解码保存图片即可。将置信度大于0.5的像素抠出来，并通过image matting技术消除锯齿
data = base64.b64decode(seg_res['foreground'])
file = open("../百度ai抠图/test.png", "wb")
file.write(data)
#分割后人像前景的scoremap，归一到0-255，不用进行二次处理，直接解码保存图片即可。Base64编码后的灰度图文件，图片中每个像素点的灰度值 = 置信度 * 255，置信度为原图对应像素点位于人体轮廓内的置信度，取值范围[0, 1]
data1 = base64.b64decode(seg_res['scoremap'])
file = open("../百度ai抠图/test1.png", "wb")
file.write(data1)
'''
分割后人像前景的scoremap,来制作云图
云图词写在黑色区域
'''
with open('../百度ai抠图/bullet.txt', encoding='utf-8') as f:
    data = f.read().split('\n')
word_counts = collections.Counter(data)
maak=255 - np.array(Image.open("../百度ai抠图/test1.png"))
#bg=np.array(Image.open("mask_1.png")) #544X960
mycloud=WordCloud(
	background_color='black',  # 设置背景颜色  默认是black
	#mask=mask_,  # 自定义蒙版
	mode='RGBA',
	mask=maak,
	max_words=500,
	font_path='simhei.ttf',  # 设置字体  显示中文
).generate_from_frequencies(word_counts)
plt.imshow(mycloud)
plt.axis("off")
mycloud.to_file('test2.png')