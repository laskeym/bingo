==========================
Bingo Card Generator/Game
==========================

Summary
========

Scope of project is to implement a Bingo Card generator.  Once this is complete, may try to implement the game itself.

Ideas
======

* The card object itself should be a matrix.  Could use nested list or possibly NumPy/Pandas.
* Could associate BINGO to 01234.  Not sure to have values in a list or dict.  B = 0: 1-15, I = 1: 16-30...ect.

Flow
======

* For now, Game will instantiate a list of BingoCards and ask how many to generate.
* Game will have winning structure
* Game will call out a number every second
* Bingo Card will have 2 matricies.  One to hold the numbers and the other to hold the hits
* As numbers are called and they are in the first matrix.  THe second one will be marked as a hit.
* Compare hit numbers to winning structure. 
  ** Hit numbers will be a list of tuplees
  ** WInning structure will be a list of list of tuples.
  ** Iterate over winning strucutre, turn list to set and intersect that against hit number list as set.
  


TO DO
=======

* Restructure Bingo Card to be a list of lists of tuples.  The second element in the tuple will represent if the number has been called.
* Create a winning structure.  For example a column of all B's would be: ([0][0], [0][1], [0][2], ...)
* Check users bingo card against winning structure

Completed
==========

* Bingo Card generator
  ** Used list of lists(matrix) as structure to hold BINGO numbers.  For example, the first list is all numbers associated with 'B'.
  ** Represented bingo_card as list of lists as well, but in a different manner.  All lists in list are composed of BINGO i.e [4, 26, 42, 49, 66]
