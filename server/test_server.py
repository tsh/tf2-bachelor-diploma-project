import unittest

class TestConnectionMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper1(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper2(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper3(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper4(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper5(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper1(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper11(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper21(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper31(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper41(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper51(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper1(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_upper2(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper12(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper22(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper32(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper42(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper52(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper12(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper112(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper212(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper312(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper412(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_upper512(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper2(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()