# Visual Sort

Visual Sort is a program will let you visualize different sorting algorithms and generate beautiful videos with sound. 
You can view some examples in the videos folder.

![merge](/examples/Merge30.gif)
![quickR](/examples/QuickR30.gif)

Supported algorithms are:
- Bogo Sort
- Bubble Sort
- Cocktail Shaker Sort
- Comb Sort
- Counting Sort
- Gnome Sort
- Insertion Sort and alternate
- Merge Sort (subarrays and in place)
- Pigeonhole Sort
- Quick Sort and alternate
- Radix Sort
- Selection Sort
- Shell Sort
- Tim Sort

Requires ffmpeg to generate video from frames and add sound.

Video files are named following this schema:

`"{algorithmName} {elements}-{fps} video.mp4"`

And this for rainbow mode videos:

`"{algorithmName} R {elements}-{fps} video.mp4"`


## Installation
Clone the repository to your computer:
```
git clone https://github.com/SauravC99/VisualSort.git
```


## Usage
Run with `-h` to see the list of commands:
```
python3 visualSort.py -h
```
Run with `-l` to see the list of algorithms:
```
python3 visualSort.py -l
```

### Quickstart
Run with no flags or variables to use the default options:
- 10 elements
- 60 frames per second
- Insertion sort algorithm
```
python3 visualSort.py
```

### Flags and Variables
There are a number of flags and variables you can add or change to generate different types of videos.

`-h` - Displays the help menu.

`-l` - Displays the list of sorting algorithms.

`-lv` - Displays the list of sorting algorithms with more detail.

`-a ALGORITHM` - Specify which sorting algorithm you want to visualize. Default is insertion sort.

`-n NUMBER` - Specify the number of elements you want to visualize sorting. Default is 10.

`-f FPS` - Specify how many frames per second the video will run at. Default is 60. Lower numbers will make the video slower. Higher numbers will make the video faster.

`-r` - Visualize in rainbow mode.


## Rainbow mode
You can run any algorithm with the `-r` flag to sort the colors of the rainbow.
![mergeR](/examples/MergeR60.gif)
![radixR](/examples/RadixR60.gif)
![shellR](/examples/ShellR70.gif)
![countingR](/examples/CountingR50.gif)
![quickR2](/examples/QuickR50.gif)


## Examples
```
python3 visualSort.py -n 30 -a quicksort
```
Will generate a video of 30 elements being sorted using quicksort at the default 60 fps.
```
python3 visualSort.py -n 30 -a quicksort -r
```
Will generate the same video as above but the graph will be colorful like a rainbow.
```
python3 visualSort.py -n 20 -a selectionsort -f 90
```
Will generate a video of 20 elements being sorted using selection sort at 90 fps. This will speed up the video.

--------------------

![tim](/examples/Tim50.gif)
![bubble](/examples/Bubble15.gif)
![selection](/examples/Selection20.gif)
![insertion](/examples/Insertion20.gif)
![bogo](/examples/Bogo5.gif)
![shell](/examples/Shell30.gif)
![radix](/examples/Radix30.gif)
![quick](/examples/Quick40.gif)