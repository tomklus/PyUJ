import queue
import unittest


class TestQueue(unittest.TestCase):

    def setUp(self): pass

    def test_empty(self):
        myQ = queue.Queue()
        self.assertTrue(myQ.is_empty())

    def test_full(self):
        myQ = queue.Queue()
        for x in range(myQ.n-1):
            myQ.put(x)
        print(myQ.n)
        self.assertTrue(myQ.is_full())

    def test_get(self):
        with self.assertRaises(IndexError):
            myQ = queue.Queue()
            myQ.get()

    def test_put(self):
        with self.assertRaises(IndexError):
            myQ = queue.Queue()
            for x in [1,2,3,4,5,6,7]:
                myQ.put(x)



    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy