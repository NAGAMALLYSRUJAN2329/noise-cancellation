import librosa
import streamlit as st
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import os
from prediction import predict_output

# data=librosa.load('audio/noise2023.wav')[0]
# prediction=predict_output(data)
# print(prediction)

st.title("NOISE CANCELLATION")
input_audio = st.file_uploader("Choose a file", type=["wav"])
if st.button('Clean the audio file'):
    st.header('Listen your file :sound:')
    st.audio(input_audio)
    data=librosa.load(input_audio)[0]
    plt.plot(data)
    # plt.xlabel('Time')
    # plt.ylabel('Amplitude')
    # plt.title('Waveform')
    # st.pyplot(plt)
    prediction=predict_output(data)
    # print(prediction)
    plt.plot(prediction)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Waveform')
    st.header('Magic of _Noise Cancellation_')
    st.pyplot(plt)
    st.warning('In some cases if the amplitude of the audio file is low it may consider it as noise and clear the required audio so keep it in mind')
    # st.write(prediction)
    if os.path.exists("audio\demo.wav"):
        os.remove("audio\demo.wav")
        sf.write("audio\demo.wav", prediction, 22050)
    else:
        sf.write("audio\demo.wav", prediction, 22050)
    st.header('Listen the denoised file :sound:')
    st.audio("audio\demo.wav",format='wav')
    # st.download_button('Download clean audio',prediction)
