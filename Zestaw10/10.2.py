import stack
import unittest


class TestStack(unittest.TestCase):

    def setUp(self): pass
    
    def test_empty(self):
        myStack = stack.Stack()
        self.assertTrue(myStack.is_empty())


    def test_pop(self):

        with self.assertRaises(IndexError):
            myStack = stack.Stack()
            myStack.pop()

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
