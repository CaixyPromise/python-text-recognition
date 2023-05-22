from app.public import public
from flask import render_template, request, send_file, jsonify, after_this_request
from config_message.Environment import SECRET_KEY, SAVE_PATH
from paddleocr import PaddleOCR, draw_ocr 
import pyttsx3
import os
from time import sleep, time
from app.utils import audio_server, pcm2wav

ocr = PaddleOCR(use_gpu=True)

@public.route('/ocr', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(code=403, message='No file part'), 403
    # 接收图片文件
    file = request.files['file']
    if file.filename == '':
        return jsonify(code=403, message='No selected file'), 403
    file.save(file.filename)

    # 图片转文字内容
    result = ocr.ocr(file.filename)
    # 文字内容输出到字符串内
    text = ' '.join([line_info[-1][0] for line_info in result])

    # 文字转语音
    time_str = audio_server.text2audio(text)
    if time_str is not False:
        os.remove(file.filename)  # 删除用户上传的图片
        # 返回音频
        return jsonify(code = 200, message = time_str), 200  # 将语音文件发送回用户
    else:
        return jsonify(code=403, message='生成语音失败!!'), 200

@public.route('/download', methods = ['POST'])
def download_file():
    # 文件路径
    filename = request.get_json().get('name')
    if filename is None:
        return jsonify(code = 403, message = 'Invalid JSON data: "name" field not found'), 403
    wav_path = f'{SAVE_PATH}/wav/{filename}.wav'
    pcm_path = f'{SAVE_PATH}/pcm/{filename}.pcm'

    @after_this_request
    def delete_file(response):
        # 删除音频文件
        if os.path.exists(wav_path):
            os.remove(wav_path)
        if os.path.exists(pcm_path):
            os.remove(pcm_path)
        return response

    # 返回音频文件
    return send_file(wav_path, as_attachment=True), 200
    
