# -*- coding: UTF-8 -*-
"""
"""
import cv2
import os

# 输出视频的保存路径
video_dir = './result2.mp4'
# 帧率
fps = 30
# 图片尺寸
img_size = (544, 960)

fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')  # opencv3.0 mp4会有警告但可以播放
videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
img_files = os.listdir('./wordcloud2')

for i in range(1, 101):
    img_path = './wordcloud2/' +'wordcloud_{}.png'.format(i)
    frame = cv2.imread(img_path)
    frame = cv2.resize(frame, img_size)   # 生成视频   图片尺寸和设定尺寸相同
    videoWriter.write(frame)      # 写进视频里
    print(f'======== 按照视频顺序第{i}张图片合进视频 剩余{888-i}========')

videoWriter.release()   # 释放资源
