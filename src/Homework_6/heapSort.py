def heapify(numArr, sizeArr, i):
    largest = i
    leftIndex = 2 * i + 1
    rightIndex = 2 * i + 2

    if leftIndex < sizeArr and numArr[leftIndex] > numArr[largest]:
        largest = leftIndex

    if rightIndex < sizeArr and numArr[rightIndex] > numArr[largest]:
        largest = rightIndex

    if largest != i:
        numArr[largest], numArr[i] = numArr[i], numArr[largest]

        heapify(numArr, sizeArr, largest)


def heapSort(numArr):
    sizeArr = len(numArr)

    for i in range(sizeArr // 2 - 1, -1, -1):
        heapify(numArr, sizeArr, i)

    for i in range(sizeArr - 1, 0, -1):
        numArr[0], numArr[i] = numArr[i], numArr[0]
        heapify(numArr, i, 0)
        
    return numArr
