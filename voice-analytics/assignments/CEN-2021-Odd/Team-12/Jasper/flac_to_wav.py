import librosa
import os

os.makedirs("wavfiles/audio")

for i in os.listdir("./dataset/audio"):
    x , sr = librosa.load("./dataset/audio/"+i, sr = 16000)
    write("./wavfiles/audio/"+i.split('.')[0]+".wav",sr,x)