from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
#using subarray
class MergeSort(InterfaceSortAlgo):
    def sort(self, arr):
        self.mergesort(arr, 0, len(arr) - 1)

    def mergesort(self, arr, left, right):
        if left < right:
            mid = left + (right - left) // 2

            self.mergesort(arr, left, mid)
            self.mergesort(arr, mid + 1, right)

            self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        arrL = [0] * (n1)
        arrR = [0] * (n2)

        for i in range(0, n1):
            arrL[i] = arr[left + i]
        for j in range(0, n2):
            arrR[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if arrL[i] <= arrR[j]:
                arr[k] = arrL[i]
                i += 1
            else:
                arr[k] = arrR[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = arrL[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = arrR[j]
            j += 1
            k += 1

    def getName(self):
        return "Merge Sort (subarrays)"