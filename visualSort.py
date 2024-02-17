import time
import numpy as np
import scipy as sp
import subprocess

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from ArrayTracker import ArrayTracker
from GenerateSoundData import GenerateSoundData

from algorithms.BubbleSort import BubbleSort
from algorithms.InsertionSort import InsertionSort
from algorithms.QuickSort import QuickSort


plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (12, 8)
plt.style.use("dark_background")

FPS = 60 #upper limit fps
#FPS = 30
#FPS = 120
#FPS = 90
#FPS = 240


#Audio Parameters
#sample frequency
FREQ_SAMPLE = 44100
OVERSAMPLE = 2

RAINBOW = False
#RAINBOW = True

N = 30
arr = np.round(np.linspace(50, 1000, N), 0)
np.random.seed(0)
np.random.shuffle(arr)

arr = ArrayTracker(arr)


t0 = time.perf_counter()

#e = BubbleSort()
#e = InsertionSort()
e = QuickSort()
e.sort(arr)

dt = time.perf_counter() - t0

arr.check(RAINBOW)

print(f"{e.getName()}")
print(f"Array sorted in {dt * 1000:.3f} ms") #multiply by 1000 sec -> ms and round to 3 decimal points

#######################################################
soundFile = f"z{e.getName()}_sound.wav"
vidFile = f"z{e.getName()}Vid.mp4"
#######################################################


s = GenerateSoundData(FPS, FREQ_SAMPLE, OVERSAMPLE)
wav_data = s.generate(arr)

sp.io.wavfile.write(soundFile, s.getFreqSample(), wav_data)


fig, ax = plt.subplots()
if not RAINBOW:
    container = ax.bar(np.arange(0, len(arr), 1), arr.full_copies[0], align="edge")
else:
    #width 1.0 to make rainbow graph look nicer
    container = ax.bar(np.arange(0, len(arr), 1), arr.full_copies[0], align="edge", width=1.0)
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value")
ax.set_title(f"{e.getName()}", loc="left")
#Make axes ticks and numbers blank
ax.set_xticks([])
ax.set_yticks([])

colorDict = {}
color = plt.colormaps["gist_rainbow"].resampled(N)
for i in range(N):
    key  = arr.full_copies[-1][i]
    num = np.interp(i, [0, N], [0, 1])
    value = color(num)
    colorDict[key] = value

def updateFrame(frame):

    ax.set_title(f"{e.getName()} - {arr.compare_arr[frame]} comparisons, {frame} accesses", loc="left")

    index, operation = arr.GetActivity(frame)

    if not operation == "check":
        for rectangle, height in zip(container.patches, arr.full_copies[frame]):
            rectangle.set_height(height)
            if not RAINBOW:
                rectangle.set_color("#1f77b4") #default color
            else:
                rectangle.set_color(colorDict[int(height)])

    if operation == "get":
        container.patches[index].set_color("white")
    elif operation == "set":
        container.patches[index].set_color("red")
    elif operation == "check":
        container.patches[index].set_color("forestgreen")
    elif operation == "checkR":
        container.patches[index].set_color("white")

    #:05.0f format to 5 digits and pad with 0s
    fig.savefig(f"frames/{e.getName()}_frame{frame:05.0f}.png", bbox_inches="tight", pad_inches=0.4)

    return(*container, )


print("Generating frames")
t0 = time.perf_counter()

ani = FuncAnimation(fig=fig, func=updateFrame, frames=range(len(arr.full_copies)),
                    blit=True, interval=1000.0/FPS, repeat=False)


#ani.save(vidFile)

for i in range(1, len(arr.full_copies)):
    updateFrame(i)

dt = time.perf_counter() - t0
if dt > 60:
    print(f"{len(arr.full_copies)} frames generated in {dt / 60:.3f} min")
else:
    print(f"{len(arr.full_copies)} frames generated in {dt:.3f} sec")


print("Making movie")
t0 = time.perf_counter()

cmd = [ 'ffmpeg', '-loglevel', 'quiet', '-y',
        '-r', f'{int(FPS)}',
        '-i', f'frames/{e.getName()}_frame%05d.png',
        '-i', f'{soundFile}',
        '-c:v', 'libx264', '-preset', 'veryslow',
        '-c:a', 'aac', '-crf', '0',
        '-map', '0:v', '-map', '1:a', f'{vidFile}']
subprocess.call(cmd)

dt = time.perf_counter() - t0
print(f"Made movie in {dt:.3f} sec")

print("deleting sound file")
a = ["rm", f"{soundFile}"]
subprocess.call(a)
print("deleting frames folder")
b = ["rm", "-r", "frames"]
subprocess.call(b)
print("making folder")
c = ["mkdir", "frames"]
subprocess.call(c)