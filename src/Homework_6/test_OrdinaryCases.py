from src.Homework_6.heapSort import heapSort


def test1():
   assert heapSort([0, 10, 8, 9, 3, 4]) == [0, 3, 4, 8, 9, 10]


def test2():
   assert heapSort([1, 5, 4, 3, 8, 7]) == [1, 3, 4, 5, 7, 8]


def test3():
   assert heapSort([10, -1, 8]) == [-1, 8, 10]
  
