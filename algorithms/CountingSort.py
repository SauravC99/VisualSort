from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class CountingSort(InterfaceSortAlgo):
    def sort(self, arr):
        max1 = max(arr.arr)
        max1 = int(max1)
        n = len(arr)
        count = [0] * (max1 + 1)
        output = [0] * (n)

        for i in range(0, n):
            count[int(arr[i])] += 1
        
        for i in range(1, max1 + 1):
            count[i] += count[i - 1]

        for i in range(len(output) - 1, -1, -1):
            output[count[int(arr[i])] - 1] = arr[i]
            count[int(arr[i])] -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def getName(self):
        return "Counting Sort"