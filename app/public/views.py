from app.public import public
from flask import render_template, request, send_file
from config_message.Environment import SECRET_KEY
from paddleocr import PaddleOCR, draw_ocr 
import pyttsx3
import os
# from flask_wtf import csrf
from time import sleep
ocr = PaddleOCR(use_gpu=True)

# @csrf.exempt
@public.route('/ocr', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    file.save(file.filename)

    result = ocr.ocr(file.filename)
    text = ' '.join([line_info[-1][0] for line_info in result])

    engine = pyttsx3.init()
    save_path = os.path.join(os.getcwd(), 'output.mp3')
    print(f'save_path: {save_path}')
    engine.save_to_file(text, save_path)
    engine.runAndWait()

    while not os.path.exists(save_path):
        sleep(0.5)

    os.remove(file.filename)  # 删除用户上传的图片
    return send_file(save_path, as_attachment=True)  # 将语音文件发送回用户

