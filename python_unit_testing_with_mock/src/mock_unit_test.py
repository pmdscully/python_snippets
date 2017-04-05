"""
    Example Module to do Py 2.7 unit testing with the 'unittest' and 'mock' APIs.
    
    Mock exists to remove the need to create stub classes to replace functionality in your unit tests.
    It captures method calls and enables assertions about those calls, enabling sub-system and 
    unit testing to remain separated. 
    (https://mock.readthedocs.io/en/latest/)
    (https://docs.python.org/dev/library/unittest.mock.html)
    
    - Install mock with: 'pip install mock'
    
    Run as: 'python mock_unit_test.py'
"""

import unittest
from mock import Mock

def square(a):
    return a*a

class MockSquare():
    def square(self, a):
        return a*a

def mock_square(obj,value):
    value += 1
    return obj.square(value)


class MyPyTest(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue( square(1)==1 ) 

    def test_2(self):
        self.assertTrue( square(2)==4 ) 

    def test_3(self):
        self.assertTrue( square(3)==9 ) 
        
    def test_obj(self):
        obj = MockSquare()
        self.assertTrue( obj.square(4)==16 ) 

    def test_mock_obj(self):
        my_mock = Mock()
        mock_square(my_mock, 3)
        my_mock.square.assert_called_with( 4 )
        # mock object
        # .
        # name of member function on the mock object expected to be called
        # .
        # argument value expected to be passed into object's member function.


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase( MyPyTest )
    unittest.TextTestRunner(verbosity=3).run(suite)
