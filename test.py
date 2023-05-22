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
# 请求文字识别，并在服务器内生成音频文件
response = requests.post(url, files=files)
# 如果生成成功
if response.status_code == 200:
    ret_json = response.json()
    print(f'response return: {response.json}')
    json_data['name'] = ret_json['message']
    # 请求下载音频文件
    response = requests.post(download_url, headers = headers, json = json_data)
    if (response.status_code == 200):
        with open(f"{ret_json['message']}.wav", 'wb') as f:
            f.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
else:
    print("Error:", response.status_code, response.text)