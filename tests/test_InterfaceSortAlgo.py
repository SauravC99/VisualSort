import pytest
from InterfaceSortAlgo import InterfaceSortAlgo
from visualSort import AlgoList

ALGORITHMS = [a for a in AlgoList]

# Test that all sorting algorithms implement methods
@pytest.mark.parametrize("algo", ALGORITHMS)
def test_interface2(algo):
    instance = algo.value

    assert isinstance(instance, InterfaceSortAlgo)

    assert hasattr(instance, 'sort'), f"{algo.name} does not implement sort()"
    assert callable(instance.sort)

    assert hasattr(instance, 'getName'), f"{algo.name} does not implement getName()"
    assert callable(instance.getName)