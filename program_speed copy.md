How to make your application fast enough.

Why? user satisfaction, energy efficiency ($$, climate), ...

Single Computer Approaches
--------------------------


- T(n) < C*f(n)   for all n > N0

- first, analyze your program to discover where you are on this scale

  1 < log n < n  < n log n < n^2 < 2^n

  try to discover better algorithm / data structure that moves
  you further to the left of this list (EC504)

  example: sorting of numbers. 
     O(n log n) merge sort, quicksort
     O(n)       bucket sort / radix sort.


- optimize your speed with a profiler

- switch to a more optimized version of same language (e.g. pypy.org)

- use specialized optimized libraries:
   - numpy / scipy
   - numba https://numba.pydata.org/

- switch to a compiled language (e.g. C++ EC602) or even assembly/machine code.


- use more than one core (multiprocessing, threading)

- coroutines, microthreads: greenlet, eventlet
- asyncio (synchronizing between threads)

- GPU programming graphics card: cuda (EC527)

- parallel computing / supercomputers (EC526)


Multiple Computer Approaches
----------------------------

- cloud computing (EC528) (eg. data mining)
- peer-to-peer massive problem sharing. (SETI)

- server (e.g google, microsoft, amazon  or bitcoin mining.)

