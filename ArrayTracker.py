import numpy as np

class ArrayTracker():

    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []
        self.comparisons = 0
        self.compare_arr = []
        self.track(0, "nothing") #for default frame at begining

    def track(self, key, accessType):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(accessType)
        self.full_copies.append(np.copy(self.arr))
        self.compare_arr.append(self.comparisons)

    def GetActivity(self, index=None):
        if isinstance(index, type(None)):
            return [(i, operation) for (i, operation) in zip(self.indices, self.access_type)]
        else:
            return (self.indices[index], self.access_type[index])

    def check(self):
        self.track(0, "nothing") #add empty frame to reset colors
        for i in range(len(self.arr)):
            self.track(i, "check")

    def __getitem__(self, key):
        self.track(key, "get")
        self.comparisons += 1
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __len__(self):
        return self.arr.__len__()