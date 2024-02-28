from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
#in place merge sort
class MergeSort(InterfaceSortAlgo):
    def sort(self, arr):
        self.mergesort(arr, 0, len(arr) - 1)

    def mergesort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2

            self.mergesort(arr, left, mid)
            self.mergesort(arr, mid + 1, right)

            self.merge(arr, left, mid, right)

    def merge(self, arr, start, mid, end):
        start2 = mid + 1

        if arr[mid] <= arr[start2]:
            return
        
        while start <= mid and start2 <= end:
            if arr[start] <= arr[start2]:
                start +=1
            else:
                value = arr[start2]
                index = start2

                while index != start:
                    arr[index] = arr[index - 1]
                    index -= 1
                
                arr[start] = value

                start += 1
                mid += 1
                start2 += 1

    def getName(self):
        return "Merge Sort (in place)"