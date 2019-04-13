"""
Example of executable package

usage:
python -m demo_reader test.bz2

"""

from demo_reader.multi_reader import MultiReader

import sys

r = MultiReader(sys.argv[1])
print(r.read())