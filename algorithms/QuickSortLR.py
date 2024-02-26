from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class QuickSortLR(InterfaceSortAlgo):
    def sort(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)

    def quicksort(self, arr, low, high):
        p = self.pivot(low, high)
        pivot = arr[p]
        i = low
        j = high
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                if p == i:
                    p = j
                elif p == j:
                    p = i
                i += 1
                j -= 1
        if low < j:
            self.quicksort(arr, low, j)
        if i < high:
            self.quicksort(arr, i, high)

    def pivot(self, low, high):
        return (low + high) // 2
    
    def getName(self):
        return "Quick Sort (LR pointers)"