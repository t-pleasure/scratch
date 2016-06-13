import unittest
from conway import *

class TestTrackers(unittest.TestCase):

  # tests conversion between numbers and array of numbers
  def test_num_conversions(self):
    self.assertEquals(num2array(123), [1,2,3])
    self.assertEquals(num2array(10001), [1,0,0,0,1])
    self.assertEquals(num2array(0), [0])
    self.assertRaises(AssertionError, num2array, -10001)

    self.assertEquals(array2num([1,2,3]), 123)
    self.assertEquals(array2num([1,0,0,0,1]), 10001)
    self.assertEquals(array2num([1,1]), 11)
    self.assertEquals(array2num([100,1]), 1001)

  # tests sequence function
  def test_look_n_say(self):
    self.assertEquals(sequence(10), [1,11,21,1211,111221,312211,13112221,1113213211,31131211131221,13211311123113112211])
  
