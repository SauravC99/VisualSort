from InterfaceSortAlgo import InterfaceSortAlgo

#implements InterfaceSortAlgo
class CocktailSort(InterfaceSortAlgo):
    def sort(self, arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        while swapped:
            swapped = False

            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    swapped = True

            if not swapped:
                break
            swapped = False
            end -= 1

            for i in range(end-1, start-1, -1):
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    swapped = True

            start += 1

    def getName(self):
        return "Cocktail Sort"