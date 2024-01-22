name = "Bubble"
def BubbleSort(arr):
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
        
d = [2,6,3,7,8,45,9,5,75,98,6,4,-2,-6,0,1]
BubbleSort(d)
print(d)