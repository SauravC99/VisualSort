from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class RadixSort(InterfaceSortAlgo):
    def sort(self, arr):
        max1 = max(arr.arr)
        exponent = 1
        while max1 / exponent >= 1:
            self.countingSort(arr, exponent)
            exponent *= 10

    def countingSort(self, arr, exponent):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] // exponent
            index = int(index)
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exponent
            index = int(index)
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def getName(self):
        return "Radix Sort"