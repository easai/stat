# Test class for median.py
import unittest
import median
import random

class TestMedian(unittest.TestCase):
     def test_menian(self):
        testList = []
        for i in range(1000):
            testList.append(random.randint(0,1000))
        res = median.median(testList)
        print(testList)
        print(f"Median: {res}")
        less = 0
        more = 0
        for item in testList:
            if item < res:
                less += 1
            elif res < item:
                more += 1
        self.assertEqual(more, less)
