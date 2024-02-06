from InterfaceSortAlgo import InterfaceSortAlgo

#implements SortAlgoInterface
class InsertionSort(InterfaceSortAlgo):
    def sort(self, arr):
        i = 1

        while i < len(arr):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                j -= 1
            i += 1

    def getName(self):
        return "Insertion Sort"