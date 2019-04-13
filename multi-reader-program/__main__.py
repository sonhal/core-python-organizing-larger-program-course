"""
Example of executable directory

useage:
python multi-reader-program test.bz2

"""

from demo_reader.multi_reader import MultiReader

import sys

r = MultiReader(sys.argv[1])
print(r.read())