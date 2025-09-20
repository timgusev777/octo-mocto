import unittest

def summoftwo(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

class TestMath(unittest.TestCase):
    def test_summoftwo_1(self):
        self.assertEqual(summoftwo([3, 3], 6), [0, 1])

    def test_summoftwo_2(self):
        self.assertEqual(summoftwo([2,7,11,15], 9), [0, 1])

    def test_summoftwo_3(self):
        self.assertEqual(summoftwo([3,2,4], 6), [1, 2])

unittest.main(argv=[''], verbosity=2, exit=False)