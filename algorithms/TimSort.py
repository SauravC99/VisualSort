from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class TimSort(InterfaceSortAlgo):
    def sort(self, arr):
        n = len(arr)
        minRun = self.calculateMinRun(n)

        for start in range(0, n, minRun):
            end = min(start + minRun - 1, n - 1)
            self.insertionSort(arr, start, end)

        size = minRun
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
                if mid < right:
                    self.merge(arr, left, mid, right)
            size = 2 * size

    def calculateMinRun(self, n):
        r = 0
        #changed to 8 to make better videos
        #while n >= 32:
        while n >= 8:
            r = r | n & 1
            n = n >> 1
        return n + r
    
    def insertionSort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            j = i
            while j > left and arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                j -= 1

    def merge(self, arr, left, mid, right):
        len1 = mid - left + 1
        len2 = right - mid
        arrL = []
        arrR = []

        for i in range(0, len1):
            arrL.append(arr[left + i])
        for i in range(0, len2):
            arrR.append(arr[mid + 1 + i])
        
        i  = 0
        j = 0
        k = left

        while i < len1 and j < len2:
            if arrL[i] <= arrR[j]:
                arr[k] = arrL[i]
                i += 1
            else:
                arr[k] = arrR[j]
                j += 1
            k += 1
        
        while i < len1:
            arr[k] = arrL[i]
            k += 1
            i += 1
        while j < len2:
            arr[k] = arrR[j]
            k += 1
            j += 1

    def getName(self):
        return "Tim Sort"