import unittest
import Program
from Logic import logic

class Test_Program(unittest.TestCase):
    def test_ReversedListwith5Parameters(self):
        testList = []
        testList.append("cat")
        testList.append("sat")
        testList.append("mat")
        testList.append("fat")
        testList.append("rat")
        result = logic.ReversedList(self, testList)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 1)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], "rat")
        self.assertEqual(result[1], "fat")
        self.assertEqual(result[2], "mat")
        self.assertEqual(result[3], "sat")
        self.assertEqual(result[4], "cat")

    def test_ReversedListwithlessThan2Parameters(self):
        testList = []
        testList.append("cat")
        result = logic.ReversedList(self, testList)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "error:Enter atleast 2 words")
        


if __name__ == '__main__':
    unittest.main()
