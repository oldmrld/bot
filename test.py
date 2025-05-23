from vosk import Model, KaldiRecognizer
import wave

model_path = "./models/vosk-model-small-ru-0.22"
audio_path = "test.wav"

model = Model(model_path)
wf = wave.open(audio_path, "rb")
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())