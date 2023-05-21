from app.public import public
from flask import render_template

from config_message.Environment import ACCESS_KEY
from paddleocr import PaddleOCR, draw_ocr
import pyttsx3
import os
ocr = PaddleOCR(use_gpu=True)

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
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

    os.remove(file.filename)  # 删除用户上传的图片
    return send_file('output.mp3', as_attachment=True)  # 将语音文件发送回用户

if __name__ == "__main__":
    app.run(port=5000, debug=True)
