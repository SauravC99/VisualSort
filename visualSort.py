import time
import numpy as np

import matplotlib.pyplot as plt



plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (12, 8)


N = 10
arr = np.round(np.linspace(50, 1000, N), 0)
np.random.seed(0)
np.random.shuffle(arr)



fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1), arr)
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value")



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
print(f"Array sorted in {dt * 1000:.3f} ms") #multiply by 1000 to get ms and go to 3 decimal points



fig, ax = plt.subplots()
container = ax.bar(np.arange(0, len(arr), 1), arr, align="edge")
ax.set_xlim([0, N])
ax.set(xlabel="Index", ylabel="Value")
