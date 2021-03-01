from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '23716532'
API_KEY = 'vistREym6409Q9Ie88F1P3sq'
SECRET_KEY = 'OIvUVcGD1nhBiuZw8YlWdqKLx2U37tw9'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('23.jpg')

""" 调用通用文字识别（高精度版） """
client.basicAccurate(image)

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
a=client.basicAccurate(image, options)
'''
将返回数据组，提取文字写入result.txt文件中
'''
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write('')
#清空result.txt
text=a['words_result']
n=len(text)
for i in range(2,n):
    with open('result.txt','a',encoding='utf-8') as file:
        file.write(text[i]['words'])
        file.write('\n')
    file.close()