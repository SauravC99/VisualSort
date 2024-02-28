import random
from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class BogoSort(InterfaceSortAlgo):
    def sort(self, arr):
        n = len(arr)
        #loops 400 times max so program wont run forever
        for _ in range(400):
            if not self.isSorted(arr):
                self.shuffle(arr)
            else:
                break

    def isSorted(self, arr):
        n = len(arr)
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    
    def shuffle(self, arr):
        n = len(arr)
        for i in range(0, n):
            r = random.randint(0, n - 1)
            arr[i], arr[r] = arr[r], arr[i]
    
    def getName(self):
        return "Bogo Sort"