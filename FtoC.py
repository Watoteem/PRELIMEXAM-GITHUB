import unittest

def conversion(a,b,y,z):

    return (a-b)*(y/z)

class TestMultiply(unittest.TestCase):

    def test(self):
        self.assertEqual((32-0)*(5/9),0)

if __name__ == '__main__':
    unittest.main()
#FtoC = (32-32)*(5/9)
#print("Conversion: ",FtoC)