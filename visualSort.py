import time
import numpy as np
import scipy as sp

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ArrayTracker import ArrayTracker
from GenerateSoundData import GenerateSoundData

from algorithms.BubbleSort import BubbleSort
from algorithms.InsertionSort import InsertionSort



plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (12, 8)

FPS = 60.0 #upper limit fps
#FPS = 50.0
#FPS = 30.0
#FPS = 120.0


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

#e = BubbleSort()
e = InsertionSort()
e.sort(arr)

dt = time.perf_counter() - t0

arr.check()

print(f"{e.getName()} Sort")
print(f"Array sorted in {dt * 1000:.3f} ms") #multiply by 1000 to get ms and round to 3 decimal points




s = GenerateSoundData(FPS, FREQ_SAMPLE, OVERSAMPLE)
wav_data = s.generate(arr)

sp.io.wavfile.write(f"zzz{e.getName()}_sound.wav", s.getFreqSample(), wav_data)


fig, ax = plt.subplots()
container = ax.bar(np.arange(0, len(arr), 1), arr.full_copies[0], align="edge")
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value", title=f"{e.getName()} Sort")
text = ax.text(0, 1000, "")



def updateFrame(frame):

    text.set_text(f" {arr.compare_arr[frame]} comparisons, {frame} accesses")

    index, operation = arr.GetActivity(frame)

    if not operation == "check":
        for rectangle, height in zip(container.patches, arr.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#1f77b4") #default color

    if operation == "get":
        container.patches[index].set_color("magenta")
    elif operation == "set":
        container.patches[index].set_color("red")
    elif operation == "check":
        container.patches[index].set_color("forestgreen")

    fig.savefig(f"frames/{e.getName()}_frame{frame:05.0f}.png") #:05.0f format to 5 digits and pad with 0s

    return(*container, text)

ani = FuncAnimation(fig=fig, func=updateFrame, frames=range(len(arr.full_copies)),
                    blit=True, interval=1000.0/FPS, repeat=False)


ani.save("zzztestVid.mp4")