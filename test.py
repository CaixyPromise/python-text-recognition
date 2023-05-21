# from paddleocr import PaddleOCR, draw_ocr
# import os
# os.environ['KMP_DUPLICATE_LIB_OK']='True'

# # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
# img_path = './imgs/11.jpg'
# result = ocr.ocr(img_path, cls=True)
# for line in result:
#     print(line)

# # 显示结果
# from PIL import Image

# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# print("".join(txts))
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')


import requests

url = 'http://127.0.0.1:6006/ocr'
files = {'file': open(r'./imgs/11.jpg', 'rb')}

response = requests.post(url, files=files)

if response.status_code == 200:
    with open('output.mp3', 'wb') as f:
        f.write(response.content)
else:
    print("Error:", response.status_code, response.text)