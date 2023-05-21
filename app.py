import pyttsx3


text = '我是谁？12312ASASNLJKAD. Hello World'
engine = pyttsx3.init(driverName='espeak')
engine.setProperty('encoding', 'utf-8')  # 设置为UTF-8编码
engine.setProperty('espeak-data-path', './zh_dict')
engine.setProperty('rate', 150)  # 设置语速为150
engine.setProperty('volume', 0.7)  # 设置音量为0.7
engine.save_to_file(text, 'output.wav')
engine.runAndWait()
import sys
print(sys.getdefaultencoding())