from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class SelectionSort(InterfaceSortAlgo):
    def sort(self, arr):
        jMin = 0

        for i in range(len(arr) - 1):
            jMin = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[jMin]:
                    jMin = j
            temp = arr[i]
            arr[i] = arr[jMin]
            arr[jMin] = temp

    def getName(self):
        return "Selection Sort"