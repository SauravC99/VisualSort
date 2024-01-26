import time
import numpy as np
import scipy as sp
from scipy.io import wavfile

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ArrayTracker import ArrayTracker

from algorithms.BubbleSort import BubbleSort



plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (12, 8)

#FPS = 60.0 #upper limit fps
#FPS = 50.0
FPS = 30.0


#Audio Parameters
#sample frequency
FREQ_SAMPLE = 44100
OVERSAMPLE = 2


N = 30
arr = np.round(np.linspace(50, 1000, N), 0)
np.random.seed(0)
np.random.shuffle(arr)

arr = ArrayTracker(arr)




t0 = time.perf_counter()

e = BubbleSort()
e.sort(arr)

dt = time.perf_counter() - t0

print(f"{e.getName()} Sort")
print(f"Array sorted in {dt * 1000:.3f} ms") #multiply by 1000 to get ms and round to 3 decimal points

#map the value to a frequency between 360 and 1200 Hz
def frequency_map(x, x_min=50, x_max=1000, frequency_min=360, frequency_max=1200):
    return np.interp(x, [x_min, x_max], [frequency_min, frequency_max])

def frequency_sample(frequency, dt=1.0/60.0, samplerate=44100, oversample=2):
    middle_samples = int(dt * samplerate)
    padded_samples = int((middle_samples * (oversample - 1) / 2))
    total_samples = middle_samples + 2 * padded_samples

    sin_wave = np.sin(2 * np.pi * frequency * np.linspace(0, dt, total_samples))

    sin_wave[0:padded_samples] = sin_wave[0:padded_samples] * np.linspace(0, 1, padded_samples)
    sin_wave[-padded_samples: ] = sin_wave[len(sin_wave)-padded_samples: ] * np.linspace(1, 0, padded_samples)

    return sin_wave


wav_data = np.zeros(int(FREQ_SAMPLE * len(arr.values) * 1.0 / FPS), dtype=float)
#num of values in a chunk (sample length)
dN = int(FREQ_SAMPLE * 1.0 / FPS)

for i, value in enumerate(arr.values):
    freq = frequency_map(value)
    sample = frequency_sample(freq, 1.0 / FPS, FREQ_SAMPLE, oversample=OVERSAMPLE)

    index_0 = int((i + 0.5) * dN - len(sample) / 2)
    index_1 = index_0 + len(sample)

    try:
        wav_data[index_0 : index_1] += sample
    except ValueError:
        pass

sp.io.wavfile.write(f"zzz{e.getName()}_sound.wav", FREQ_SAMPLE, wav_data)


"""
name = "Insertion"
t0 = time.perf_counter()
i = 1
while (i < len(arr)):
    j = i
    while (j > 0 and arr[j - 1] > arr[j]):
        temp = arr[j - 1]
        arr[j - 1] = arr[j]
        arr[j] = temp
        j -= 1
    i += 1

dt = time.perf_counter() - t0
print(dt)

print(f"{name} Sort")
print(f"Array sorted in {dt * 1000:.3f} ms")
"""
"""
np.random.shuffle(arr)

name = "Quick"
def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i

t0 = time.perf_counter()
quicksort(arr, 0, len(arr) - 1)
dt = time.perf_counter() - t0
print(dt)

print(f"{name} Sort")
print(f"Array sorted in {dt * 1000:.3f} ms")
"""


fig, ax = plt.subplots()
container = ax.bar(np.arange(0, len(arr), 1), arr, align="edge")
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value", title=f"{e.getName()} Sort")
text = ax.text(0, 1000, "")



def updateFrame(frame):

    text.set_text(f" Accesses = {frame}")
    for rectangle, height in zip(container.patches, arr.full_copies[frame]):
        rectangle.set_height(height)
        rectangle.set_color("#1f77b4") #default color

    index, operation = arr.GetActivity(frame)
    if operation == "get":
        container.patches[index].set_color("magenta")
    elif operation == "set":
        container.patches[index].set_color("red")

    fig.savefig(f"frames/{e.getName()}_frame{frame:05.0f}.png") #:05.0f format to 5 digits and pad with 0s

    return(*container, text)

ani = FuncAnimation(fig=fig, func=updateFrame, frames=range(len(arr.full_copies)),
                    blit=True, interval=1000.0/FPS, repeat=False)


ani.save("zzztestVid.mp4")#################