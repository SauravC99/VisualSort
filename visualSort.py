import time
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class ArrayTracker():

    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def track(self, key, accessType):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(accessType)
        self.full_copies.append(np.copy(self.arr))

    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)
    
    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __len__(self):
        return self.arr.__len__()



plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (12, 8)

FPS = 30.0 #upper limit fps

N = 10
arr = np.round(np.linspace(50, 1000, N), 0)
np.random.seed(0)
np.random.shuffle(arr)

arr = ArrayTracker(arr)





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
name = "Bubble"
t0 = time.perf_counter()
n = len(arr)
for i in range(n):
    swapped = False
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            swapped = True
    if not swapped:
        break
dt = time.perf_counter() - t0
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
ax.set(xlabel="Index", ylabel="Value")



def updateFrame(frame):

    for rectangle, height in zip(container.patches, arr.full_copies[frame]):
        rectangle.set_height(height)

    return(*container,)

ani = FuncAnimation(fig=fig, func=updateFrame, frames=range(len(arr.full_copies)),
                    blit=True, interval=1000.0/FPS, repeat=False)


ani.save("test.gif")