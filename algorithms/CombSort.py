from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class CombSort(InterfaceSortAlgo):
    def sort(self, arr):
        n = len(arr)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = self.getNextGap(gap)
            swapped = False
            for i in range(0, n - gap):
                if arr[i] > arr[i + gap]:
                    temp = arr[i]
                    arr[i] = arr[i + gap]
                    arr[i + gap] = temp
                    swapped = True

    def getNextGap(self, gap):
        g = (gap * 10) // 13
        if g < 1:
            return 1
        return g

    def getName(self):
        return "Comb Sort"