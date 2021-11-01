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

def main():
  # print('\nbasegroup tests')
  # for grouptest in [ ['3','4','21','7'], ['100','4','5'], ['6','7','21']]:
  #   res = basegroup(grouptest)
  #   print(grouptest,res)
  print(base_convert(7))




if __name__ == '__main__':
  main()