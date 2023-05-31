import pyaudio
import wave
import base64
from math import cos, pi
import numpy as np
import os
import librosa
import librosa.display

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print(5 * "*" + "recording" + 5 * "*")
    frames = []
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print(5 * "*" + "done" + 5 * "*")
    except Exception as exp:
        print(str(exp))
    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return sample_width, frames


def record_to_file(file_path):
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def proc(audio_path):
    wr = wave.open('test.wav', 'r')
    par = list(wr.getparams())
    par[3] = 0
    ww = wave.open(audio_path, 'w')
    ww.setparams(tuple(par))
    lowpass = 75
    highpass = 2000
    sz = wr.getframerate()
    c = int(wr.getnframes() / sz)
    for num in range(c + 1):
        data = np.frombuffer(wr.readframes(sz), dtype=np.int16)
        left, right = data[0::2], data[1::2]
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf[:lowpass], rf[:lowpass] = 0, 0
        lf[highpass:], rf[highpass:] = 0, 0
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
        ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
        if (num == 0):
            a = ns
        else:
            a = np.concatenate((a, ns), axis=0)
    for i in range(len(a)):
        hamming_value = 0.54 - 0.46 * cos((2 * pi * i) / (len(a) - 1))
        a[i] = hamming_value * a[i]
    ww.writeframes(a.tostring())
    wr.close()
    ww.close()
    os.remove('test.wav')


def find_distance(filename1, filename2):
    y1, sr1 = librosa.load(filename1)
    mfcc1 = librosa.feature.mfcc(y1, sr=sr1)
    y2, sr2 = librosa.load(filename2)
    mfcc2 = librosa.feature.mfcc(y2, sr=sr2)
    from numpy.linalg import norm
    from dtw import dtw
    dist, cost, d, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
    os.remove(filename2)
    return dist


def encrypt(string):
    string = string.encode("UTF-8")
    string = base64.b64encode(string)
    string = string.decode("UTF-8")
    return string
