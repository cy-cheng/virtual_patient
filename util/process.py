import speech_recognition as sr
import util.dialog as dialog

def process_audio(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='zh-TW')
            return text
        except sr.UnknownValueError:
            dialog.error("無法辨認您的語音，請再試一次", "test")
        except sr.RequestError:
            dialog.error("翻譯系統無法運作", "test")

