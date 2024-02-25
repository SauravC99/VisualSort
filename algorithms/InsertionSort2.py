from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class InsertionSort2(InterfaceSortAlgo):
    def sort(self, arr):
        for i in range(len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                j -= 1

    def getName(self):
        return "Insertion Sort 2"