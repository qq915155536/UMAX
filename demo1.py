import unittest
from unittest import mock






class Test_01(unittest.TestCase):
    def test_case(self):
        res1=mock.Mock(return_value=1)
        res2=mock.Mock(return_value=2)
        print(res2)
        print(type(res2),res2)



if __name__ == '__main__':
    unittest.main()
