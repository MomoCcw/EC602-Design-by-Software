"bigint checker"
import unittest
import time
import logging
import subprocess as sub
import random
import os
import math
import random
import numpy as np
import sys
from threading import Thread

from queue import Queue, Empty


# 2.1 use curl_grading



VERSION, CURL_GRADING_VER = (2,1), (3, 2)

def update_curl_grading():
    print('updating curl_grading')
    from requests import get
    r = get('https://curl.bu.edu/static/content/curl_grading.py')
    with open('curl_grading.py','w') as f:
        f.write(r.text)

def get_curl_grading():
    from os import listdir
    files = listdir();
    if "curl_grading.py" not in files:
        update_curl_grading()

    import curl_grading as e
    if e.VERSION < CURL_GRADING_VER:
        update_curl_grading()
        from importlib import reload
        e = reload(e)

    return e

curl_grading = get_curl_grading()

programs = ['bigint.cpp']

tested_programs = {x:x for x in programs}


TIMEALLOWED = 1
COMPILEALLOWED = 2

P={"stdout":sub.PIPE,"timeout":TIMEALLOWED,"stderr":sub.PIPE}

CP={"stdout":sub.PIPE,"timeout":COMPILEALLOWED,"stderr":sub.PIPE}




bigintmain="""
#include <iostream>
#include <vector>
#include "bigint.h"

int main() {
  BigInt A, B;

  std::cin >> A >> B;

  std::cout << multiply_int(A, B) << std::endl;
}
"""

SmallIntTests=[(8,9),(4,5),(999,1001)]

BigIntTests=[(123456,123456),(10000100060043,34444234234),(10**19-1,10**19-1),
(100000001,9900000099)]

ZeroTests=[(12340,0),(0,23342342)]

def compile(cpp,executable):
  return ['g++','-std=c++17',cpp, '-o', executable]
          
        
def check_bi_mult(self,thetest,testcases):
    points_per_case = self.Points[thetest]/len(testcases)
    self.Points[thetest] = 0 
    for (a,b) in testcases:
      atimesb = a*b
      with self.subTest(CASE=" {} * {} = {}".format(a,b,atimesb)):
       intext="{} {}".format(a,b).encode()
       T = sub.run([self.executable],input=intext,**P)
       res = T.stdout.decode().strip()
       if res != str(atimesb):
         self.fullfail("your multiply: {}\ncorrect answer: {}\n".format(res,atimesb))
       else:
        self.Points[thetest] += points_per_case 



class bigintTestCase(unittest.TestCase):
    "bigint.cpp"
    @classmethod
    def setUpClass(cls):
        cls.Penalty = {'authors':50,'libraries':50,'brackets':50}
        cls.Points = {"a":40,"b":40,'c':20,"style":1}
        cls.MaxPoints = cls.Points.copy()
        cls.authorlimit = 2
        cls.valid_includes = set(['vector','string',"bigint.h"])

        cls.refcode = {'lines':36,'words':165}
        cls.msgs=[]
        cls.realfilename = tested_programs[cls.__doc__]
        cls.file_contents_main = bigintmain

        curl_grading.compile_separate(cls,"st3_big")


    def fullfail(self,test,msg):
      self.Points[test] = 0
      self.fail(msg)


    test_libraries = curl_grading.test_libraries
    test_authors = curl_grading.test_authors
    test_style = curl_grading.test_cppstyle
    test_brackets = curl_grading.bracket_check

    def test_mult(self):
       "a. test small numbers"
       check_bi_mult(self,"a",SmallIntTests)

    def test_big_mult(self):
       "b. test big numbers"
       check_bi_mult(self,"b",BigIntTests)

    def test_zero_mult(self):
       "c. test mult by zero"
       check_bi_mult(self,"c",ZeroTests)

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.executable)
        except:
            pass
        curl_grading.stylegrade(cls)


testcases={
'bigint.cpp':bigintTestCase,
}


programs = ["bigint.cpp"]

tested_programs = {x:x for x in programs}

if __name__ == '__main__':
    print('HW9 Bigint Checker Version {0}.{1}\n'.format(*VERSION))
    g = {}
    for prog in testcases:
        report, g[prog] = curl_grading.check_program(testcases[prog])
        print(f"----report for {prog}----",report,f"----end report {prog}----",sep="\n")
    print('\nGrade Summary')
    for prog in testcases:
      print(prog,g[prog])

