import speech_recognition

# 创建 Recognizer 对象
r = speech_recognition.Recognizer()

# 开始语音识别
while True:
    # 从麦克风读取语音
    with speech_recognition.Microphone() as source:
        print("请开始说话...")
        audio = r.listen(source)

    # 使用 Recognizer 对象将语音转换成文本
    text = r.recognize_sphinx(audio)

    # 输出识别结果
    print("识别结果：", text)

    # 判断用户是否需要退出
    while True:
        choice = input("是否继续？(Y/N)")
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            exit()
        else:
            print("无效输入，请重新输入！")
