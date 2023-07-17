import librosa
import streamlit as st
import soundfile as sf
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import os
from prediction import predict_output
# import pyaudio
# import wave

select = st.sidebar.radio(
    "Navigation",
    ("Recorded", "Live")
)
if select=="Recorded":
    st.title("NOISE CANCELLATION")
    input_audio = st.file_uploader("Choose a file", type=["wav"])
    if st.button('Clean the audio file',key="CleanRecording"):
        st.header('Listen your file :sound:')
        st.audio(input_audio)
        data=librosa.load(input_audio)[0]
        plt.plot(data)
        prediction=predict_output(data)
        plt.plot(prediction)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        st.header('Magic of _Noise Cancellation_')
        st.pyplot(plt)
        st.warning('In some cases if the amplitude of the audio file is low it may consider it as noise and clear the required audio so keep it in mind')
        if os.path.exists("audio\demo.wav"):
            os.remove("audio\demo.wav")
            sf.write("audio\demo.wav", prediction, 22050)
        else:
            sf.write("audio\demo.wav", prediction, 22050)
        st.header('Listen the denoised file :sound:')
        st.audio("audio\demo.wav",format='wav')
        # st.download_button('Download clean audio',prediction)

if select=="Live":
    st.title("NOISE CANCELLATION")


    # audio=pyaudio.PyAudio()
    # stream=audio.open(format=pyaudio.paInt16,channels=1,rate=22050,input=True,frames_per_buffer=1)
    # frames=[]

    # if st.button('Start recording'):
    #     st.write("Recording...")
    #     bool=st.button('Stop recording',key='stopbutton')
    #     while not bool:
    #         print("hello")
    #         # data=stream.read(1024)
    #         # frames.append(data)
    #         bool=st.button('Stop recording',key='stopbutton')

    # stream.stop_stream()
    # stream.close()
    # audio.terminate()
    # # sf.write("audio\recording.wav", np.array(frames), 22050)

    # sound_file=wave.open('audio/recording.wav','wb')
    # sound_file.setnchannels(1)
    # sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    # sound_file.setframerate(22050)
    # sound_file.writeframes(b''.join(frames))
    # sound_file.close()


    # chunk = 1024 
    # sample_format = pyaudio.paInt16  
    # channels = 1
    # fs = 22050
    # seconds = st.number_input("Enter the duration:")
    # filename = "audio/ecording.wav"

    # if st.button('Start recording'):
    #     p = pyaudio.PyAudio()

    #     st.write('Recording...')

    #     stream = p.open(format=sample_format,
    #                     channels=channels,
    #                     rate=fs,
    #                     frames_per_buffer=chunk,
    #                     input=True)

    #     frames = []

    #     for i in range(0, int(fs / chunk * seconds)):
    #         data = stream.read(chunk)
    #         frames.append(data)

    #     stream.stop_stream()
    #     stream.close()
    #     p.terminate()

    #     st.write('Finished recording')

    #     wf = wave.open(filename, 'wb')
    #     wf.setnchannels(channels)
    #     wf.setsampwidth(p.get_sample_size(sample_format))
    #     wf.setframerate(fs)
    #     wf.writeframes(b''.join(frames))
    #     wf.close()
    #     st.audio("audio\ecording.wav",format='wav')


    sample_rate=22050
    duration=st.number_input("Enter the duration:")
    dtype='float32'
    if st.button('Start recording'):
        st.write("Recording...") 
        record_voice=sd.rec(int(duration*sample_rate), samplerate=sample_rate,channels=1,dtype=dtype)
        sd.wait()
        st.write("Recording stopped")
        if os.path.exists("audio\ecording.wav"):
                os.remove("audio\ecording.wav")
        sf.write("audio\ecording.wav", record_voice, 22050)
        st.audio("audio\ecording.wav",format='wav')


    # duration=1
    # if st.button('Start recording'):
    #     st.write("Recording...")
    #     bool=st.checkbox('Stop recording',key='stopbutton')
    #     record_voice=sd.rec(int(duration*sample_rate), samplerate=sample_rate,channels=1,dtype=dtype)
    #     sd.wait()
    #     # record_voice=np.reshape(record_voice,(22050,-1))
    #     record_voice=record_voice.flatten()
    #     while not bool:
    #         st.write("Hello")
    #         st.write(record_voice.shape)
    #         st.write(record_voice)
    #         voice=sd.rec(int(duration*sample_rate), samplerate=sample_rate,channels=1,dtype=dtype)
    #         sd.wait()
    #         # bool=st.button('Stop recording',key='stopbutton')
    #         # voice=np.reshape(voice,(22050,-1))
    #         voice=voice.flatten()
    #         record_voice=np.concatenate((record_voice,voice),axis=0)
    #         # if os.path.exists("audio\ecording.wav"):
    #         #     os.remove("audio\ecording.wav")
    #         st.write(record_voice.shape)
    #         st.write(record_voice)
    #         sf.write("audio\ecording.wav", record_voice, 22050)
    #     st.write("Recording stopped")
    #     st.audio("audio\ecording.wav",format='wav')


    if st.button('Clean the audio file',key="CleanLive"):
        st.header('Listen your file :sound:')
        st.audio("audio\ecording.wav")
        data=librosa.load("audio\ecording.wav")[0]
        plt.plot(data)
        prediction=predict_output(data)
        plt.plot(prediction)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        st.header('Magic of _Noise Cancellation_')
        st.pyplot(plt)
        st.warning('In some cases if the amplitude of the audio file is low it may consider it as noise and clear the required audio so keep it in mind')
        if os.path.exists("audio\demo.wav"):
            os.remove("audio\demo.wav")
            sf.write("audio\demo.wav", prediction, 22050)
        else:
            sf.write("audio\demo.wav", prediction, 22050)
        st.header('Listen the denoised file :sound:')
        st.audio("audio\demo.wav",format='wav')
        # st.download_button('Download clean audio',prediction)
