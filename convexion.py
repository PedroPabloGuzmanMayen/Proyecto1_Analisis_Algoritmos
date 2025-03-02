def encode1s(number):
  number = int(number)
  toconcatenate = ''
  for i in range (0,number):
    toconcatenate+= '1'
  return toconcatenate

def decode1s(number):
  return len(number)

def replaced(s):
    s = s.replace("B", "").replace("b", "")
    return decode1s(s)