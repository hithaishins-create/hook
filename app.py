import unittest
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(80,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(10,10),10)
  def test_multiply(self):
    self.assertEqual(multiply(6,5),30)
if __name__ == "__main__":
  print("student calculator application")
  print("Addition:",add(20,20))
  print("Subtraction:",subtract(20,10))
  print("Multiplication:",multiply(5,4))
  print("\nExecuting Automated Test...\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)
    
