# Copyright --your info here.
#


class Wedding: 
    def __init__(self):
      pass
    def shuffle(self, guests):
      pass
    def barriers(self, guests, bars):
      pass


def  show_result(v, partial=False):
  v.sort()
  print("",len(v),"\n".join(v),sep="\n")



def standard_tests():
  standard = Wedding()
  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("WXYZ")
  show_result(res)

  res = standard.shuffle_barriers("xyz", [0])
  show_result(res)

  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("abcdefXY")
  show_result(res)

  res = standard.shuffle_barriers("abcDEFxyz", [2, 5, 7])
  show_result(res)

  res = standard.shuffle_barriers("ABCDef", [4])
  show_result(res)

  res = standard.shuffle_barriers("bgywqa", [0, 1, 2, 4, 5])
  show_result(res)

  res = standard.shuffle_barriers("n", [0])
  show_result(res)
  res = standard.shuffle("hi")
  show_result(res)



def main():

  print("""Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
""")
  w = Wedding()
  while True:
    asktype=input().split()
    if asktype[0] == "quit":
      break;
    elif asktype[0] == "tests":
      standard_tests()
    elif asktype[0] == "s":
      guests = asktype[1]
      r = w.shuffle(guests)
      show_result(r);
    elif asktype[0] == "b":
      guests,nbar,bars = asktype[1],asktype[2],asktype[3:]
      r = w.barriers(guests, bars)
      show_result(r)
    elif asktype[0] == "sp":
      guests,ind = asktype[1:]
      r = w.shuffle(guests);
      show_result(r, True, ind);
    elif asktype[0] == "bp":
      guests,nbar,bars,ind  = asktype[1],asktype[2],asktype[3:-1],asktype[-1]
      r = w.barriers(guests, bars)
      show_result(r, True, ind)
    

if __name__ == '__main__':
  main()