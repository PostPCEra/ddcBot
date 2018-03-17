#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:55:45 2018

@author:  
"""
# -------------------  Code Gems from web ---------------------------
#
# -------------------  *****************  -------------------------import timeit


# Macros, Batch renaming of variables & Multi-cursors  in Pycharm editor
#    https://stackoverflow.com/questions/39746405/is-there-a-keyboard-shortcut-in-pycharm-for-renaming-a-specific-variable
# Macros : there are pre-built macros :  compl -> comprehension for List , compd -> dictionary , iter etcc.
#   - type 'compl' & TAB key to select , or 'comp' will show all matching one as list , you pick
#   - you can also define your own, see  Pycharm->Preferences -> Editor -> Live Templates
#
# Batch renaming of vars : select a var , SHIFT + fn+ f6 , will highlight others , start modifying
# Multi-cursors : place a cursor, hold <ALT Option> key and 'mouse click' all other places . Then start editing
# Best part : all these edit are  can be UNDO or REDO  under Edit menu ... cool

# MAC Keyboard keys : which symbols corresponds to which key board ..
# ^ (caret) key : this is <CTRL> or <Control> key
# --\__  key : ths is <alt option> key

# Methods navigation :
# on editor ,in the scroll bar Gutter , the horizantal lines each represent a Method, so click on those to go to methods
#

# understanding Lists very well
even_odd = [[], []]
for i in range(10):
    even_odd[i % 2 == 1].append(i)

print(even_odd)

# https://docs.python.org/2/library/timeit.html
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 10000 loops, best of 3: 0.22 sec per loop ; # this is fastest execution time, that is lower time
timeit.timeit('"-".join(map(str, range(100)))', number=10000)

# https://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-a-list
lst = [1, 2, 3, 4, 4, 5, 5, 6, 1]
freq_two_or_more = [x for x in lst if lst.count(x) > 1]
uniq = set(freq_two_or_more)  # removes duplicates
print(uniq)  # {1, 4, 5}


# https://stackoverflow.com/questions/43698531/sorting-a-zipped-object-in-python-3
l1 = [3, 9, 2, 24, 1, 6]
l2 = ['a', 'b', 'c', 'd', 'e']
zp = zip(l1, l2)

slist = sorted(zp, key=lambda p: p[1])  # sorting  based on the values of y in each (x,y) pair , for x sort use p[0]
print(slist)  # [(3, 'a'), (9, 'b'), (2, 'c'), (24, 'd'), (1, 'e')]

# https://stackoverflow.com/questions/14466068/sort-a-list-of-tuples-by-second-value-reverse-true-and-then-by-key-reverse-fal
from operator import itemgetter
#d.sort(key=itemgetter(0))
#d.sort(key=itemgetter(1), reverse=True)

# Dictionary List search : https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
people = [{'name': 'Tom', 'age': 10}, {'name': 'Mark', 'age': 5}, {'name': 'Pam', 'age': 7}]
result = [ row for row in people if row['name'] == 'Pam']
result = [ row for row in people if row.get('name2222', '') == 'Pam'] # greaceful no execption if 'name2222' don't exists
if len(result):
    print(result[0])


# sort Dictionary : convert to List, use functools lib
# https://stackoverflow.com/questions/5213033/sort-list-of-list-with-custom-compare-function-in-python
import functools
dict1 = {'adult': [20, 58], 'child': [2, 6, 12], 'teen': [13, 15, 19]}

cat_lst = list(dict1.items())
print(cat_lst)

def docompare(item1, item2):   # can be any user defined function name, two elements of the list are passed each time
    val1, val2 = item1[1], item2[1]
    return val1[0] - val2[0]  #  should return one of ( negative, 0 , postive number ), this is basis for comparision

sl = sorted(cat_lst, key=functools.cmp_to_key(docompare))
print(sl)
# [('child', [2, 6, 12]), ('teen', [13, 15, 19]), ('adult', [20, 58])]


# Sorting and Grouping Nested Lists in Python :
# https://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python

x = [
 ['4', '21', '1', '14', '2008-10-24 15:42:58'],
 ['3', '22', '4', '2somename', '2008-10-24 15:22:03'],
 ['5', '21', '3', '19', '2008-10-24 15:45:45'],
 ['6', '21', '1', '1somename', '2008-10-24 15:45:49'],
 ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
]

from operator import itemgetter
x.sort(key=itemgetter(1))

from itertools import groupby
for elt, items in groupby(x, itemgetter(1)):
    print(elt, items)
    for i in items:
        print(i)

# Enumerate(lst) is the crux of all 'nested Lists' manipulation Filtering etc..
# this works well, the next code given in url seems over kill
filter_list = [row for i, row in enumerate(x) if row[3] == '2somename']


from pprint import pprint as pp
y = groupby(x, itemgetter(1))  # Now y is an iterator containing tuples of (element, item iterator).
pp([y for y in x if y[3] == '2somename'])


# --------------  Pathlib ------------------------
# http://pbpython.com/pathlib-intro.html
# One of python’s strengths is that it continues to develop and grow over time. The pathlib module is a prime example
# of the care that the maintainers take to build new capabilities that improve the overall capabilities of python

from pathlib import Path

in_file_1 = Path.cwd() / "in" / "input.xlsx"
out_file_1 = Path.cwd() / "out" / "output.xlsx"

# Finally, there is one other trick you can use to build up a path with multiple directories:
parts = ["in", "input.xlsx"]
in_file_3 = Path.cwd().joinpath(*parts)

dir_to_scan = "/media/chris/KINGSTON/data_analysis"
p = Path(dir_to_scan)
p.is_dir()  # True
p.is_file()  # False
p.parts   # ('/', 'media', 'chris', 'KINGSTON', 'data_analysis')
p.absolute()  # PosixPath('/media/chris/KINGSTON/data_analysis')

# See following 2 sections , on the above blog post for good examples
# Combining Pathlib and Pandas , Walking Directories


# --------------  Date & Time functions ------------------------
# https://pymotw.com/2/datetime/
import datetime

d1 = datetime.date(2008, 3, 12)
d2 = d1.replace(year=2009)  # replace any part

today = datetime.date.today()
today.year
today.month

# 1. parsing parts : getattr()
dt = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print (attr, ':', getattr(dt, attr))

# 2. Datetime arithmetic : timedelta()
oneweek = datetime.timedelta(weeks=1)  # give as number as one week worth of time
next_week = today + oneweek
prev_week = today - oneweek

# 3. Formattings between String & Date
format = "%a %b %d %H:%M:%S %Y"

s1  = today.strftime(format)  # date -> string

d = datetime.datetime.strptime(s1, format)  # string -> date : string Parse
s2 = d.strftime(format)

s1 == s2

def first_sunday_on_or_after(dt):
    days_to_go = 6 - dt.weekday()
    if days_to_go:
        dt += timedelta(days_to_go)
    return dt


# 3 rd Monday on or after dt , here n = 3,  x=0 ( monday )
def nth_xday_on_or_after(dt, n, x ):
    pass

# --------------  Global Variable ------------------------
# https://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them?rq=1
globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print(globvar)       # Prints 1


# sample.py
myGlobal = 5

def func1():
    myGlobal = 42

def func2():
    print(myGlobal)

func1()
func2() # prints 5

# --------------------------    ---------------------------------------------------


# https://stackoverflow.com/questions/16628088/euclidean-algorithm-gcd-with-multiple-numbers
from fractions import gcd
lis = [3, 6, 9, 12]
result = gcd(*lis[:2])  # get the gcd of first two numbers ( unpack list as parameters with * )
if len(lis) >2:
    for x in lis[2:]:    # now iterate over the list starting from the 3rd element
        result = gcd(result,x)
print(result)

# --------------------------    ---------------------------------------------------
# Date logic
# https://stackoverflow.com/questions/35490420/how-to-check-type-of-object-in-python

# https://pymotw.com/2/datetime/

def process_dates(dtstr1, dtstr2):

    formatstr = ''
    def string_to_dt(dtstr):
        format1, format2 = "%Y-%m-%d", "%m-%d-%Y"
        try:
            dt = datetime.datetime.strptime(dtstr, format1)  # if exception , try format2
            formatstr = format1
        except ValueError:
            dt = datetime.datetime.strptime(dtstr, format2)
            formatstr = format2

        return dt, formatstr

    d2, formatstr = string_to_dt(dtstr2)
    d1, _      = string_to_dt(dtstr1)
    delta = d2 - d1
    print(delta.days, delta.seconds)
    dd = d1 + delta
    print(delta)
    print(formatstr)

# https://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes

import datetime
#dstr1 = '01-15-2018'
#dstr2 = '04-18-2018'
dstr1 = '2018-01-15'
dstr2 = '2018-04-18'

#process_dates(dstr1, dstr2)

