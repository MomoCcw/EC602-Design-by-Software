# Copyright 2021 Chuwei Chen chenchuw@bu.edu

"""
Problem Description
-------------------

A ciphertext is the result of encrpytion performed on
a message, called "plaintext"

Here is the encryption algorithm we will implement:

  Each letter a-z and A-Z is transformed in a two step process:

   1. Replace the letter by its "opposite letter" in the alphabet. So a becomes z,
       b becomes y, c becomes x, etc
   2. Adjust the new letter by an offset. If the offset is 2, then every letter is 
   "moved up" in the alphabet by 2, i.e. a becomes c, b becomes d, and so on. 
   (z becomes b i.e. we wrap around)

Other rules:
  1. Characters other than a-z and A-Z are not modified.
  2. The offset is initially 0. Whenever a certain letter appears in the plaintext,
  the offset changes to the count of that letter. The change to the offset is 
  effective for the next letter in the plaintext.
  3. Lower and upper cases should be maintained.
  4. Both the lower and upper case version of the key cause the offset to change.
  5. If the key is not a letter, it should still cause changes to the offset when
     it appears in the plaintext.


Hints:
------
use the built in functions chr and ord


Assignment
----------
Write a function "decoder" that will convert ciphertext back into plaintext.

Both are strings.

This is the function signature:

def decoder(ciphertext, key):

or more formally

def decoder(ciphertext : str, key : str) -> str:

Although key is a string, if it is not a single character, an exception
should be raised by the function.

"""


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





cipher_plain_examples = {('abcde', 'z'): ('zyxwv', 'z'), ('abcde', 'c'): ('zyxxw', 'c'), ('this is plaintext', 'i'): ('gsri sj mqbtpjyfj', 'i'), ('This Is Plaintext', 'i'): ('Gsri Sj Mqbtpjyfj', 'i'), ('This Is Plaintext', 'I'): ('Gsri Sj Mqbtpjyfj', 'I'), ('I am sending 100 dollars, right now.', 'n'): ('R zn hvmxsnv 100 ynqqbkj, ktvui oog.', 'n'), ('This is a poem.\nAbout nothing,\nat all', ','): ('Gsrh rh z klvn.\nZylfg mlgsrmt,\nah app', ','), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a'): ('zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg', 'a'), (None, 'bad key'): ('gsrh urmzo vcznkov droo izrhv zm vcxvkgrlm', 'bad key')}

def main():
  for example,key in cipher_plain_examples:
    cipher,key = cipher_plain_examples[(example,key)]
    try:
      plain = decoder(cipher,key)
    except:
      plain = None
    print(example,key)
    print(cipher)
    print("output:",plain)
    # plain == example
    print(plain==example)
    print()


if __name__ == '__main__':
  main()