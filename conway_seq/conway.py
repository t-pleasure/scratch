"""
The Look and say sequence is a recursively defined sequence of numbers studied most notably by John Conway.
Sequence Definition:
Take a decimal number
Look at the number, visually grouping consecutive runs of the same digit.
Say the number, from left to right, group by group; as how many of that digit there are - followed by the digit grouped.
This becomes the next number of the sequence.
An example:
Starting with the number 1, you have one 1 which produces 11.
Starting with 11, you have two 1's i.e. 21
Starting with 21, you have one 2, then one 1 i.e. (12)(11) which becomes 1211
Starting with 1211 you have one 1, one 2, then two 1's i.e. (11)(12)(21) which becomes 111221
Task description:
Write a program to generate successive members of the look-and-say sequence up to the provided parameter N.
"""

def num2array(num):
  """
  Converts a whole number (int/long) into an array of numbers
  Inputs:
    num (int or long) -- number to be converted. Note: MUST BE >= 0.
  Outputs:
    An array of ints where each element correponds to do a digit from num.
    For example, 123 -> [1,2,3]
  """
  assert num >= 0, "input must be non negative"
  if num == 0:
    return [0]
  ret = []
  while num > 0:
    ret = [num % 10] + ret
    num = num / 10
  return ret

def array2num(a):
  """
  Converts an array of whole numbers (int/long) into a number by
  simply concatenating all the digits.
  Inputs:
    a (list[int]) -- array to be converted.
  Outputs:
    An int (or long if the number is big enough) represented by a.
    For example, [1,2,3] -> 123
  """
  return int("".join(map(str, a)))

def look_and_say(num):
  """
  Given a number, produces the look and say value for the number.
  Input:
    num (int) -- the number to evalute
  Output:
    (int or long) -- the look and say value for the input number.
  """
  assert num >= 0, "input must be non negative"
  digits = num2array(num)
  prev = digits[0]
  ctr = 1
  buffer = []
  cur = prev
  for elm in digits[1:]:
    cur = elm
    if prev == cur:
      ctr += 1
    else:
      buffer += [ctr, prev]
      prev = cur
      ctr = 1
  buffer += [ctr, cur]
  return array2num(buffer) 

def generate_sequence(n):
  """
  Produces a GENERATOR(int) of the look and say sequence up
  until the nth element.
  Intput:
    n (int) -- the number of elements to generate
  Output:
    generator<int> -- yields the look and say sequence up until the nth element.
  """
  ctr = 0
  prev = 1
  while ctr < n:
    yield prev
    ctr += 1
    prev = look_and_say(prev)

def sequence(n):
  """
  Produces the look and say sequence up until the nth element.
  Intput:
    n (int) -- the number elements in the look and say sequence to reutrn
  Output:
    list<int> -- the first n elements in the look and say sequence
  """
  return [_ for _ in generate_sequence(n)]

if __name__ == "__main__":
  while True:
    n = int(raw_input("length of look-and-say sequence to compute: ").strip())
    print "n=(%d) generates:" % n
    print sequence(n) 
