def decoder(ciphertext : str, key : str) -> str:
  if len(key) != 1:
    return None
  plain_buffer = ""
  lower = []
  upper = []
  for i in range(97,123):
    lower.append(chr(i))
  for i in range(65,91):
    upper.append(chr(i))
  lower_rev = lower.copy()
  lower_rev.reverse()
  upper_rev = upper.copy()
  upper_rev.reverse()

  for i in ciphertext:
    if i.islower():
      plain_buffer = plain_buffer + (lower[lower_rev.index(i)])
    elif i.isupper():
      plain_buffer = plain_buffer + (upper[upper_rev.index(i)])
    else:
      plain_buffer = plain_buffer + i
  
  plain_buffer = list(plain_buffer)
  # Here we have plain text, but on offset involved
  offset = 0
  for i in range(len(plain_buffer)):
    if plain_buffer[i] == key.lower() or plain_buffer[i] == key.upper():
        offset += 1 # OFFSET SHOULD BE DETERMINED AGAIN IN THE LOOP
        j = i+1
        for j in range(j,len(plain_buffer)):
          if plain_buffer[j].islower():
            if lower.index(plain_buffer[j])+1 < len(lower):
              plain_buffer[j] = lower[lower.index(plain_buffer[j])+1]
             
            else:
              plain_buffer[j] = lower[(lower.index(plain_buffer[j])+1)-26]

          elif plain_buffer[j].isupper():
            if upper.index(plain_buffer[j])+1 < len(upper):
              plain_buffer[j] = upper[upper.index(plain_buffer[j])+1]
             
            else:
              plain_buffer[j] = upper[(upper.index(plain_buffer[j])+1)-26]
  ans = "".join(plain_buffer)
  return ans

def change_asc(x:str) -> str:
  if x.islower():
    buf = 122 - ord(x)
    return chr(buf+97)
  elif x.isupper():
    buf = 90 - ord(x)
    return chr(buf+65)
  else:
    return x

# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ


def main():

  print(decoder('R zn hvmxsnv 100 ynqqbkj, ktvui oog.','n'))

if __name__ == '__main__':
  main()