import pytest
import numpy as np
from visualSort import AlgoList
from ArrayTracker import ArrayTracker

# List of algorithms except Bogosort
ALGORITHMS = [a.name for a in AlgoList if a.name != "BOGOSORT"]

@pytest.mark.parametrize("algo_name", ALGORITHMS)
def test_sorting_algorithm(algo_name):
    algo = AlgoList[algo_name].value
    arr = np.array([3, 5, 1, 2, 4])
    tracker = ArrayTracker(arr)

    algo.sort(tracker)
    expected = np.sort(arr)

    assert np.array_equal(tracker.arr, expected), f"{algo.getName()} failed to sort"
    assert len(tracker.full_copies) > 0

    name = algo.getName()
    assert isinstance(name, str)
    assert len(name) > 0