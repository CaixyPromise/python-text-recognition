import wave
from time import time
from config_message.Environment import SAVE_PATH

def pcm2wav(time_str, channels=1, bits=16, sample_rate=16000):
    # 打开 PCM 文件
    pcmf = open(SAVE_PATH + f'pcm/{time_str}.pcm', 'rb')
    pcmdata = pcmf.read()
    pcmf.close()
 
    # 打开将要写入的 WAVE 文件
    wavfile = wave.open(SAVE_PATH + f'wav/{time_str}.wav', 'wb')
    # 设置声道数
    wavfile.setnchannels(channels)
    # 设置采样位宽
    wavfile.setsampwidth(bits // 8)
    # 设置采样率
    wavfile.setframerate(sample_rate)
    # 写入 data 部分
    wavfile.writeframes(pcmdata)
    wavfile.close()
 
 
# if __name__=="__main__":
#     pcm2wav("demo.pcm", "demo.wav")