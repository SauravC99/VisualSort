import sys

sys.path.append('../VisualSort')

import pytest
import numpy as np
from ArrayTracker import ArrayTracker

# Test initialization of ArrayTracker
def test_initialization():
    arr = [1, 2, 3, 4, 5]
    tracker = ArrayTracker(arr)

    # __init__ calls reset() which calls track()

    assert len(tracker) == len(arr)
    assert list(tracker.arr) == arr
    assert list(tracker.full_copies[0]) == arr

    assert tracker.indices == [0]
    assert tracker.values == [1]
    assert tracker.access_type == ["nothing"]
    assert len(tracker.full_copies) == 1
    assert tracker.comparisons == 0
    assert tracker.compare_arr == [0]

# Test tracking with __getitem__
def test_ArrayTracker_get():
    arr = [1, 2, 3, 4, 5]
    tracker = ArrayTracker(arr)

    res = tracker[1]

    assert res == 2
    assert tracker.indices == [0, 1]
    assert tracker.values == [1, 2]
    assert tracker.access_type[-1] == "get"
    assert len(tracker.full_copies) == 2
    assert tracker.comparisons == 1
    _, op = tracker.GetActivity(1)
    assert op == "get"

# Test tracking with __setitem__
def test_ArrayTracker_set():
    arr = [1, 2, 3, 4, 5]
    tracker = ArrayTracker(arr)

    tracker[2] = 10

    assert tracker.arr[2] == 10
    assert tracker.indices == [0, 2]
    assert tracker.values == [1, 10]
    assert tracker.access_type[-1] == "set"
    assert len(tracker.full_copies) == 2
    assert tracker.comparisons == 0
    _, op = tracker.GetActivity(1)
    assert op == "set"

# Test __len__
def test_ArrayTracker_len():
    arr = [1, 2, 3, 4, 5]
    tracker = ArrayTracker(arr)

    assert len(tracker) == 5

# Test the check method
def test_ArrayTracker_check():
    arrR = [1, 2, 3]
    trackerR = ArrayTracker(arrR)

    trackerR.check(rainbow=True)
    #rainbow true goes through whole array
    assert len(trackerR.indices) == len(arrR) * 2
    accesses = trackerR.access_type[1:]
    expected = ["nothing", "checkR", "checkR", "checkR", "nothing"]
    assert accesses == expected

    arr = [1, 2, 3]
    tracker = ArrayTracker(arr)

    tracker.check(rainbow=False)
    #rainbow false adds extra every other frame
    assert len(tracker.indices) == len(arr) * 2 + 1
    accesses = tracker.access_type[1:]
    expected = ["nothing", "check", "check", "check", "check", "check"]
    assert accesses == expected

# Test the reset method
def test_ArrayTracker_reset():
    arr = [1, 2, 3, 4, 5]
    tracker = ArrayTracker(arr)

    #do some operations
    tracker[3] = 50
    a = tracker[2]
    b = tracker[1]
    tracker[4] = 100

    tracker.reset()
    assert len(tracker.indices) == 1
    assert len(tracker.values) == 1
    assert len(tracker.full_copies) == 1
    assert tracker.access_type == ["nothing"]
