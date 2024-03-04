import numpy as np
import scipy as sp
import time

import subprocess

import matplotlib.pyplot as plt

from ArrayTracker import ArrayTracker
from sound.GenerateSoundData import GenerateSoundData
from InterfaceSortAlgo import InterfaceSortAlgo

from algorithms.BogoSort import BogoSort
from algorithms.BubbleSort import BubbleSort
from algorithms.CocktailSort import CocktailSort
from algorithms.CombSort import CombSort
from algorithms.CountingSort import CountingSort
from algorithms.GnomeSort import GnomeSort
from algorithms.InsertionSort import InsertionSort
from algorithms.InsertionSort2 import InsertionSort2
from algorithms.MergeSort import MergeSort
from algorithms.MergeSort2 import MergeSort2
from algorithms.PigeonholeSort import PigeonholeSort
from algorithms.QuickSort import QuickSort
from algorithms.QuickSortLR import QuickSortLR
from algorithms.RadixSort import RadixSort
from algorithms.SelectionSort import SelectionSort
from algorithms.ShellSort import ShellSort
from algorithms.TimSort import TimSort

from enum import Enum



class AlgoList(Enum):
    BOGOSORT = BogoSort()
    BUBBLESORT = BubbleSort()
    COCKTAILSORT = CocktailSort()
    COMBSORT = CombSort()
    COUNTINGSORT = CountingSort()
    GNOMESORT = GnomeSort()
    INSERTIONSORT = InsertionSort()
    INSERTIONSORT2 = InsertionSort2()
    MERGESORT = MergeSort()
    MERGESORT2 = MergeSort2()
    PIGEONHOLESORT = PigeonholeSort()
    QUICKSORT = QuickSort()
    QUICKSORTLR = QuickSortLR()
    RADIXSORT = RadixSort()
    SELECTIONSORT = SelectionSort()
    SHELLSORT = ShellSort()
    TIMSORT = TimSort()

#Plot Parameters
plt.rcParams["font.size"] = 16
plt.rcParams["figure.figsize"] = (12, 8)
plt.style.use("dark_background")

#Audio Parameters
FREQ_SAMPLE = 44100
OVERSAMPLE = 2

#Variables
def setGlobalVariables(num, fps, rainbow):
    global N
    global FPS
    global RAINBOW

    N = num
    FPS = fps
    RAINBOW = rainbow

#make frames folder if it does not exist
def precheck():
    import os

    path = "frames/"
    if not os.path.exists(path):
        cmd = ["mkdir", "frames"]
        subprocess.call(cmd)

def run(algo: InterfaceSortAlgo):
    array = np.round(np.linspace(50, 1000, N), 0)
    np.random.seed(0)
    np.random.shuffle(array)
    array = ArrayTracker(array)

    t0 = time.perf_counter()

    algorithm = algo
    algorithm.sort(array)

    dt = time.perf_counter() - t0
    print(f"{algorithm.getName()}")
    print(f"Array sorted in {dt * 1000:.3f} ms") #multiply by 1000 sec -> ms and round to 3 decimal points

    array.check(RAINBOW)

    global soundFile
    if not RAINBOW:
        soundFile = f"{algorithm.getName()}_sound.wav"
        vidFile = f"{algorithm.getName()} {N}-{FPS} video.mp4"
    else:
        soundFile = f"{algorithm.getName()}_R_sound.wav"
        vidFile = f"{algorithm.getName()} R {N}-{FPS} video.mp4"

    sound = GenerateSoundData(FPS, FREQ_SAMPLE, OVERSAMPLE)
    soundData = sound.generate(array)
    sp.io.wavfile.write(soundFile, sound.getFreqSample(), soundData)

    fig, ax = plt.subplots()
    if not RAINBOW:
        container = ax.bar(np.arange(0, len(array), 1), array.full_copies[0], align="edge")
    else:
        #width 1.0 to make rainbow graph look better
        container = ax.bar(np.arange(0, len(array), 1), array.full_copies[0], align="edge", width=1.0)
    ax.set_xlim([0, N])
    ax.set(xlabel="Index", ylabel="Value")
    ax.set_title(f"{algorithm.getName()}", loc="left")
    #make ticks and numbers blank
    ax.set_xticks([])
    ax.set_yticks([])

    colorDict = {}
    if RAINBOW:
        color = plt.colormaps["gist_rainbow"].resampled(N)
        for i in range(N):
            key = array.full_copies[-1][i]
            num = np.interp(i, [0, N], [0, 1])
            value = color(num)
            colorDict[key] = value

    def updateFrame(frame):

        ax.set_title(f"{algorithm.getName()} - n={N} - {array.compare_arr[frame]} comparisons, {frame} accesses", loc="left")

        index, operation = array.GetActivity(frame)

        if not operation == "check":
            for rectangle, height in zip(container.patches, array.full_copies[frame]):
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
        fig.savefig(f"frames/{algorithm.getName()}_frame{frame:05.0f}.png", bbox_inches="tight", pad_inches=0.4)

        return (*container, )

    print("Generating frames")
    t0 = time.perf_counter()

    for i in range(0, len(array.full_copies)):
        updateFrame(i)

    dt = time.perf_counter() - t0
    if dt > 60:
        print(f"{len(array.full_copies)} frames generated in {dt / 60:.3f} min")
    else:
        print(f"{len(array.full_copies)} frames generated in {dt:.3f} sec")

    print("Making movie")
    t0 = time.perf_counter()

    cmd = [ 'ffmpeg', '-loglevel', 'quiet', '-y',
            '-r', f'{int(FPS)}',
            '-i', f'frames/{algorithm.getName()}_frame%05d.png',
            '-i', f'{soundFile}',
            '-c:v', 'libx264', '-preset', 'veryslow',
            '-c:a', 'aac', '-crf', '0',
            '-map', '0:v', '-map', '1:a', f'{vidFile}']
    subprocess.call(cmd)

    dt = time.perf_counter() - t0
    print(f"Made movie in {dt:.3f} sec")

def cleanup():
    print("deleting sound file")
    a = ["rm", f"{soundFile}"]
    subprocess.call(a)
    print("deleting frames folder")
    b = ["rm", "-r", "frames"]
    subprocess.call(b)
    print("making folder")
    c = ["mkdir", "frames"]
    subprocess.call(c)

def main(args):
    #default values
    n = 10
    fps = 60
    algo = InsertionSort()

    if args.number:
        n = args.number
    if args.fps:
        fps = args.fps
    if args.algorithm:
        if args.algorithm.upper() not in AlgoList.__members__.keys():
            print("Algorithm not found. Run with '-l' flag to see algorithm list")
            exit(1)
        else:
            algo = AlgoList[args.algorithm.upper()].value
        #if bogosort is chosen without specifying n, default n is 4
        if args.algorithm.upper() == "BOGOSORT" and not args.number:
            n = 4
    
    precheck()
    setGlobalVariables(n, fps, args.rainbow)
    run(algo)
    cleanup()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", action="store_true",
                        help="Display the list of sorting algorithms avaliable.")
    parser.add_argument("-lv", "--listverb", action="store_true",
                        help="Display a verbose list of sorting algorithms.")
    parser.add_argument("-a", "--algorithm",
                        help="Specify which sorting algorithm to use. Run with '-l' to see the list.")
    parser.add_argument("-n", "--number", type=int,
                        help="Specify the number of elements you want to animate sorting. Default 10.")
    parser.add_argument("-f", "--fps", type=int,
                        help="Specify how many frames per second the animation will run. Default 60.")
    parser.add_argument("-r", "--rainbow", action="store_true",
                        help="Use this flag to make the graph colorful.")
    args = parser.parse_args()

    if args.list:
        for algorithm in AlgoList:
            print(algorithm.name)
    elif args.listverb:
        for algorithm in AlgoList:
            if algorithm.name == "MERGESORT":
                print(f"{algorithm.name}        (subarrays)")
            elif algorithm.name == "MERGESORT2":
                print(f"{algorithm.name}       (in place)")
            elif algorithm.name == "QUICKSORT":
                print(f"{algorithm.name}        (right pivot)")
            elif algorithm.name == "QUICKSORTLR":
                print(f"{algorithm.name}      (LR pointers)")
            else:
                print(algorithm.name)
    else:
        main(args)