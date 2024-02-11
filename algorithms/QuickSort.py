from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class QuickSort(InterfaceSortAlgo):
    def sort(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)

    def quicksort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quicksort(arr, low, p - 1)
            self.quicksort(arr, p + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
        temp = arr[i]
        arr[i] = arr[high]
        arr[high] = temp

        return i
    
    def getName(self):
        return "Quick Sort"