from InterfaceSortAlgo import InterfaceSortAlgo

#implements SortAlgoInterface
class BubbleSort(InterfaceSortAlgo):
    def sort(self, arr):
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

    def getName(self):
        return "Bubble Sort"