from src.Homework_6.heapSort import heapSort


def testEmpty():
    assert heapSort([]) == []


def testOneElm():
    assert heapSort([5]) == [5]


def testNegativeElm():
    assert heapSort([-1, -2, -3]) == [-3, -2, -1]


def testLargeElm():
    assert heapSort([1000000000, 2000000000]) == [1000000000, 2000000000]


def testNone():
    assert heapSort(None) is None
