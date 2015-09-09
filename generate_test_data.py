#!/usr/bin/env python

# this script will read a sample sam file from stdin 
# consisting of reads from a single chromosome
# and break the chromosome up into windows of specified size
# then assign a unique identifier for each window
# and recalculate the position of the read relative
# to the window, rather than relative to the chromosome
# It outputs a new sam file with modified seq/pos info
# so we can try and assemble the windows based on barcode info
# The right answer will be "window_1 -> window_2 -> window_3 ..."

import sys
import math

WINDOW_SIZE = 10000

for line in sys.stdin:
    fields = line.strip().split()
    seq_id = fields[2]
    position = int(fields[3])
    window_number = int(math.ceil(float(position)/WINDOW_SIZE)) 
    window_id = "window_" + str(window_number)
    window_position = position - (WINDOW_SIZE * (window_number - 1))
    fields[2] = window_id
    fields[3] = str(window_position)
    sys.stdout.write("\t".join(fields) + "\n")
