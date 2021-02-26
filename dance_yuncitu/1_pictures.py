#-- coding: utf-8 --
#@Time : 2021/2/3 15:38
#@Author : XXXX
#@Email : XXXX@qq.com
#@File : pictures.py
#@Software: PyCharm
'''从视频中截取图片'''
import cv2
# print(path)
# ============================ 视频处理 分割成一帧帧图片 =======================================
cap = cv2.VideoCapture('./butterfly.mp4')
num = 1
while True:
    # 逐帧读取视频  按顺序保存到本地文件夹
    ret, frame = cap.read()
    if ret:
        if 1 <= num < 2:
            cv2.imwrite(f"./pictures/img_{num}.jpg", frame)   # 保存一帧帧的图片
            print(f'========== 已成功保存第{num}张图片 ==========')
        num += 1
    else:
        break
cap.release()   # 释放资源

