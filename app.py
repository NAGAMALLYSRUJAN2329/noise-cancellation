import librosa
from prediction import predict_output

data=librosa.load('audio/noise2023.wav')[0]

prediction=predict_output(data)
print(prediction)