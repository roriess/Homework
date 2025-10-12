import heapSort


def testEmpty():
    assert heapSort.heapSort([]) == []


def testOneElm():
    assert heapSort.heapSort([5]) == [5]


def testNegativeElm():
    assert heapSort.heapSort([-1, -2, -3]) == [-3, -2, -1]


def testLargeElm():
    assert heapSort.heapSort([1000000000, 2000000000]) == [1000000000, 2000000000]


def testNone():
    assert heapSort.heapSort(None) == None
