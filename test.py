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
file_path = './imgs/11.jpg'
access_key = 'Text Recognition'
download_url = 'http://127.0.0.1:6006/download'

files = {
    'file': open(file_path, 'rb')
}
headers = {
    'Content-Type': 'application/json'
}
json_data = {
    'name': 'example_filename'
}

response = requests.post(url, files=files)

if response.status_code == 200:
    ret_json = response.json()
    print(f'response return: {response.json}')
    json_data['name'] = ret_json['message']
    response = requests.post(download_url, headers = headers, json = json_data)
    if (response.status_code == 200):
        with open(f"{ret_json['message']}.wav", 'wb') as f:
            f.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
else:
    print("Error:", response.status_code, response.text)