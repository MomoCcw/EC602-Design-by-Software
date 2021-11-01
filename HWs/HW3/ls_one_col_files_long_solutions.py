#!/usr/bin/env python
# Copyright 2021 J Carruthers jbc@bu.edu
# solution to lshw1 problem

import datetime
import grp
import math
import os
import pwd
import sys


# ls sort order
# 1. just the letters regardless of case
# 2. lowercase preceeds uppercase
# 3. After this, sort by "letorder : symbols then $, then digits, then letters
#
# filenames with symbols """$| !"&'()*;<=>?[\^`""" require special handling
# with quotes and spacing.
#

alphalower = "".join(chr(ord('a') + x) for x in range(26))
# these symbols are considered letters and are used  by first two
# sort conditions
lets = alphalower.upper() + alphalower + '$0123456789'

# letorder is all-symbols then aAbB...zZ
letorder = ""
for therange in [range(32, 47), range(58, 65), range(91, 97), range(123, 127)]:
    for i in therange:
        letorder += chr(i)

letorder += "$0123456789"
for let in alphalower:
  letorder += let + let.upper()

Or = {letorder[ind]:ind for ind in range(len(letorder))}


def reverse_case(y):
    "switch lower and upper cases"
    return "".join(x.upper() if x.islower() else x.lower() for x in y)


def symbolsort(x):
    "convert the chars in x to their lexigraphic ordering by ls"
    return tuple(Or[c] for c in x)


def lsorder(f):
    letsonly = "".join(x for x in f if x in lets)
    return (letsonly.lower(), reverse_case(letsonly), symbolsort(f))


def quotes(x,pad=False):
    orig = x
    if '"' in x and "'" in x:
        x = x.replace("'","'\\''")
        return f"'{x}'"
    elif "'" in x:
        return f'"{x}"'
    else:
        for special in r"""$| !"&'()*;<=>?[\`^""":
            if special in x:
                return f"'{x}'"
    if x != orig:
      return x
    elif pad:
      return " "+x
    else:
      return x

def has_quoted_file(files):
    for file in files:
        if quotes(file) != file:
            return True
    return False

def get_files(noquotes=False):
    #files = [x for x in os.listdir() if not x.startswith('.')]
    files = list(filter(lambda x: not x.startswith('.'), os.listdir()))
    files.sort(key=lsorder)

    return files if noquotes else [quotes(x) for x in files]


def getcols(filecols, thefiles):
    "given the #cols, figure out the column widths and #lines required"
    numfiles = len(thefiles)
    has_quotes = has_quoted_file(thefiles)

    if numfiles % filecols==0:
        numlines = numfiles//filecols
    else:
        numlines = numfiles//filecols+1

    if (filecols-1)*numlines >=numfiles:
      return [0],None

    colwidth=[]
    for i in range(filecols):
        column_files = thefiles[i*numlines:(i+1)*numlines]
        extraspace = 1 if has_quotes else 2
        colwidth.append(max(len(quotes(x,pad=has_quotes)) for x in column_files) + extraspace)
    
    colwidth[-1] -= 1
    return colwidth, numlines


def arrange_cols(thefiles):
  "determine the arrangement of files into columns"
  "returns column widths and #lines to use"
  if os.isatty(1):
    termsize = os.get_terminal_size()
    terminal_width = termsize.columns
    filecols = 1
    while True:
      colwidth, numlines = getcols(filecols, thefiles)
      if sum(colwidth)>terminal_width:
        filecols -= 1
        break
      elif numlines==1:
        break
      else:
        filecols += 1

    colwidth, numlines = getcols(filecols, thefiles)

    while not numlines:  # some solns are invalid, go back
      filecols -=1
      colwidth, numlines = getcols(filecols, thefiles)
  else:
    filecols = 1
    colwidth, numlines = getcols(filecols, thefiles)

  return colwidth, numlines


def lsone(only_these=None):
  the_files = only_these or get_files()
  for fname in the_files:
      print(fname)


def lscol(only_these=None):
  the_files = only_these or get_files(noquotes=True)

  # determine which file names go on what line
  colwidth, numlines = arrange_cols(the_files)

  we_have_quotes = has_quoted_file(the_files)

  # use a spacing of numlines between each fname on a line.
  for i in range(numlines):
    last_one_quoted = False
    needs_space = has_quoted_file(the_files[:numlines])
    s=[0]
    for j, fname in enumerate(the_files[i::numlines]):
      quoted_file = quotes(fname)
      has_quotes = quoted_file != fname

      needs_space = has_quoted_file(the_files[j*numlines:(j+1)*numlines])
      #print(the_files[j*numlines:(j+1)*numlines],file=sys.stderr)
      #print(quoted_file,has_quotes,needs_space,file=sys.stderr)
      #if needs_space and not has_quotes:
      #  s[-1] += 1
      if last_one_quoted:
         s[-1] += 1

      s.append(quotes(fname,pad=we_have_quotes))
      s.append(colwidth[j] - len(quoted_file))
       
      last_one_quoted = fname != quoted_file

    #print(s,file=sys.stderr)
    for elem in s[:-1]:
      if isinstance(elem,int):
        print(" "*elem,end="")
      else:
        print(elem,end="")
    print()


def processargs(args):
  files_only = []
  dirs_only = []
  arg_not_found = []
  for x in args:
     if os.path.isdir(x):
      dirs_only.append(x)
     elif os.path.isfile(x) or os.path.islink(x):
      files_only.append(x)
     else:
      arg_not_found.append(x)

  files_only.sort(key=lsorder)
  dirs_only.sort(key=lsorder)
  return arg_not_found, files_only, dirs_only


def lsfiles(args):
  "implement ls with arguments"
  listfcn = lscol if os.isatty(1) else lsone

  if args:
    arg_not_found, files_only, dirs_only = processargs(args)
  else:
    arg_not_found,dirs_only = [],[]
    files_only = get_files(noquotes=True)

  for notafile in arg_not_found:
    print(f"ls: cannot access '{notafile}': No such file or directory",file=sys.stderr)

  # show the files specified, then the directories
  if files_only:
    listfcn(files_only)

  for index,thedir in enumerate(dirs_only):
    # special case: if a directory is specified, but is the only thing, dont echo
    # the dir name.
    if files_only:
      print(f"\n{thedir}:")
    elif len(dirs_only)==1:
      pass
    elif index == 0:
      print(f"{thedir}:")
    else:
      print(f"\n{thedir}:")


    files = [x for x in os.listdir(thedir) if not x.startswith('.')]
    files.sort(key=lsorder)
    displayed_files = [quotes(x) for x in files]
    listfcn(displayed_files)


def lslong(only_these=None,subdir=""):
  arg_not_found, dirs_only = [], []

  if subdir:
    files_only = only_these
  elif only_these:
      arg_not_found,files_only,dirs_only = processargs(only_these)
  else:
      files_only = get_files(noquotes=True)



  for notafile in arg_not_found:
    print(f"ls: cannot access '{notafile}': No such file or directory",file=sys.stderr)

  # do some prelim size calcs.
  maxsize=0
  total_size = 0

  for entry in files_only:
     if subdir:
        entry = subdir+"/"+entry
     statinfo = os.lstat(entry)

     fsize = statinfo.st_size
     if fsize > maxsize:
       maxsize = fsize
     total_size += statinfo.st_blocks
  size_len = len(str(maxsize))


  if not only_these or subdir:
    print(f"total {total_size//2}")
  
  need_quotes = has_quoted_file(files_only)

  for entry in files_only:
    realentry = subdir+"/"+entry if subdir else entry

    if os.path.islink(realentry):
      ftype = 'l'
    elif os.path.isdir(realentry):
      ftype = "d"
    elif os.path.isfile(realentry):
      ftype = "-"
    else:
      breakpoint()


    statinfo = os.stat(realentry) if ftype !='l' else os.lstat(realentry)

    # calculate modes
    modes = list("rwxrwxrwx")
    mode = statinfo.st_mode & (0xFFFF)
    for i in range(9):
      if mode % 2 == 0:
        modes[8-i]="-"
      mode //= 2
    modes = "".join(modes)

    fsize = statinfo.st_size
    nlinks = statinfo.st_nlink
    group = grp.getgrgid(statinfo.st_gid).gr_name
    owner = pwd.getpwuid(statinfo.st_uid).pw_name
    
    # date info
    d = datetime.datetime.fromtimestamp(statinfo.st_mtime)
    date1 = datetime.datetime.strftime(d,"%b")
    date2 = datetime.datetime.strftime(d,"%H:%M")
    datestr = f"{date1} {d.day:>2} {date2}"
    
    quoted_entry = quotes(entry)
    if need_quotes and entry == quoted_entry:
        quoted_entry = " "+entry
    
    if ftype == 'l':
      realfilename = os.readlink(realentry)
      quoted_entry = f"{quoted_entry} -> {realfilename}"
    
    thelisting = f"{ftype}{modes} {nlinks} {owner} {group} {fsize:>{size_len}} {datestr} {quoted_entry}"
    print(thelisting)

  if not subdir:
    for thedir in dirs_only:
       if len(files_only)+len(dirs_only)>1:
         print(f"\n{thedir}:")
       files = [x for x in os.listdir(thedir) if not x.startswith('.')]
       files.sort(key=lsorder)
       lslong(files,subdir=thedir)




subcommands={'lsone':lsone, 'lscol':lscol, 'lsfiles':lsfiles, 'lslong':lslong}

takesargs = ['lsfiles']

if __name__ == '__main__':
    progname = sys.argv[0]
    for x in subcommands:
      if progname.endswith(x):
        if x in takesargs:
          subcommands[x](sys.argv[1:])
        else:
          subcommands[x]()

        sys.exit()
