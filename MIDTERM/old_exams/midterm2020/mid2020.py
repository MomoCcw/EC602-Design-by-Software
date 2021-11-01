# Here are the two functions and two classes you are to complete.

def modify(L,D):
  """modify the list L based on the instructions contained in the dictionary D, as follows:
  If a value in the list L is also in the dictionary D as a key, replace the value in the list
  by the value that the key points to.
  """
  "if L[i] == D.key() -> L[i] = D.key.value"
  for i in range(0,len(L)):
    for ind, value in enumerate(D):
      if L[i] == value:
        L[i] = D.get(value)

def base_convert(x):
  ans = []
  for i in range(2,11):
    n = x
    digits = []
    while n != 0:
      digits.append(str(n%i))
      n = n//i
    digits.reverse()
    ans.append("".join(digits))
  return ans


def basegroup(x:list):
  ans_dic = {}
  for i in x:
      ans_elements = []
      for j in x:
        if j in base_convert(int(i)):
          ans_elements.append(int(j))
      if len(ans_elements) > 1:
        ans_dic[int(i)] = ans_elements
  return ans_dic


class Point():
    """represent a point in 2d space. Point(x,y) is the syntax to create."""
    def __init__(self,x=None,y=None):
        if x == None:
            self.x = 0
        else:
            self.x = x
        if y == None:
            self.y = 0
        else:
            self.y = y
    def __repr__(self):
        return f"P({self.x},{self.y})"
    def __iter__(self): #???
        yield True

class Circle():
    """represent a Circle in 2d space. Circle(x,y,radius) is the syntax to create."""
    def __init__(self,x,y,radius):
        if x == None:
            self.x = 0
        else:
            self.x = x
        if y == None:
            self.y = 0
        else:
            self.y = y
        self.radius = radius
    def __repr__(self):
        return f"Circle({self.x},{self.y},radius={self.radius})"
    def __contains__(self,point):
        dis = ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5
        if (dis < self.radius):
            return True





# this main is used to help you test and to document what these things are supposed
# to do

def main():
    # modify testing
    print('modify tests')
    L=['a','b',2,'a','c']
    D={2:"two",'a':1}
    modify(L,D)
    print('modify',L)
    L=[6, 8, 12, 6, 12,'alpha']
    D={6:"two",'alpha':42}
    modify(L,D)
    print('modify',L)
    # basegroup testing
    print('\nbasegroup tests')
    for grouptest in [ ['3','4','21','7'], ['100','4','5'], ['6','7','21']]:
      res = basegroup(grouptest)
      print(grouptest,res)

    # Circle and Point testing
    print('\nCircle/Point tests')
    points = [Point(4,6),Point(5,8),Point(4,8),Point(6.1,8),Point()]
    
    r = Circle(4,6,2.1)

    print('testing',points,'with',r)
    for q in points:
        print(q)
        if q in r:
            print(q ,'is inside of',r)
        else:
            print(q,'is outside of',r)
    print([r])



if __name__ == '__main__':
    main()