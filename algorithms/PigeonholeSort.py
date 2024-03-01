from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class PigeonholeSort(InterfaceSortAlgo):
    def sort(self, arr):
        mmin = int(min(arr.arr))
        mmax = int(max(arr.arr))
        size = mmax - mmin + 1

        holes = [0] * size

        for i in range(len(arr)):
            x = int(arr[i])
            holes[x - mmin] += 1

        i = 0
        for count in range(size):
            while holes[count] > 0:
                holes[count] -= 1
                arr[i] = count + mmin
                i += 1

    def getName(self):
        return "Pigeonhole Sort"