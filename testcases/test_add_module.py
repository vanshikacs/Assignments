import unittest

def division(a, b):
    return a / b

class TestAddModule(unittest.TestCase):
    def setUp(self):
        super().setUp()
    
    def tearDown(self):
        super().tearDown()
    
    def test_division_success(self):
        result = division(5, 2)
        self.assertEqual(result, 2.5)
    
    def test_division_failure_not_equal_2_0(self):
        result = division(5, 2)
        self.assertNotEqual(result, 2.0)
    
    def test_division_failure_not_equal_2_5(self):
        result = division(6, 2)
        self.assertNotEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()
