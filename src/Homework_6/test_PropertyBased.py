from src.Homework_6.heapSort import heapSort
from hypothesis import given, settings, HealthCheck
from hypothesis.strategies import lists, integers


def selectionSort(numArr):
    if numArr is None:
        return None
    
    for i in range(len(numArr)):
        minElmPos = i
        for k in range(i + 1, len(numArr)):
            if numArr[minElmPos] >= numArr[k]:
                minElmPos = k

        if numArr[minElmPos] != numArr[i]:
            numArr[minElmPos], numArr[i] = numArr[i], numArr[minElmPos]

    return numArr


@given(lists(integers()))
@settings(suppress_health_check = [HealthCheck.too_slow])
def test(numArr):
    assert heapSort(numArr.copy()) == selectionSort(numArr.copy())


