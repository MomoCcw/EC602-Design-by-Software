

class Season():
  def __init__(self,name=""):
    print('new season')
    self.name = name

  def __str__(self):
    return (self.name)
  # __repr__ is for list printing.!!!
  def __repr__(self): 
    return f"Season({self.name})"

  def __add__(self,other):
    return Season(" ".join([self.name,other.name]))

def main():
  a = Season('Winter')
  b = Season('Late')
  c = b + a
  d = [a,b]
  print(a, b, [c])
  print(d) # goes to __repr__

if __name__ == '__main__':
  main()