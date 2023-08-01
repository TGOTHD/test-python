# 导入必要的库
import pyttsx3
import time

# 定义语音引擎
engine = pyttsx3.init()

# 定义语音速度
engine.setProperty('rate', 150)

# 定义语音音量
engine.setProperty('volume', 1)

# 定义语音发音人
engine.setProperty('voice', 'en-us')

# 定义对话内容
dialog = '''
- Hello!
- Hi! How are you?
- I'm fine, thanks. And you?
- I'm good, too. Thank you.
'''

# 分解对话内容为句子的列表
dialog_list = dialog.split('\n')

# 遍历对话内容并播放
for sentence in dialog_list:
    # 播放语音
    engine.say(sentence)
    # 等待语音播放完成
    engine.runAndWait()
    # 暂停一段时间，以便听清上句语音
    time.sleep(1)

# 输出结果
print('语音对话结束。')