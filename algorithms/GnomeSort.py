from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class GnomeSort(InterfaceSortAlgo):
    def sort(self, arr):
        n = len(arr)
        self.gnomeSort(arr, n)

    def gnomeSort(self, arr, n):
        index = 0
        while index < n:
            if index == 0:
                index += 1
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                temp = arr[index]
                arr[index] = arr[index - 1]
                arr[index - 1] = temp
                index -= 1

    def getName(self):
        return "Gnome Sort"