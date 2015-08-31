#!/usr/bin/env python

# this script will read a sample sam file from stdin 
# and calculate the "similarity" between
# adjacent windows of the sequence, based on barcodes associated with loci.
# it's meant to help with sketching out a reasonable "similarity" metric and 
# to help characterize the data so we know what to expect.

# toward this latter end, it'll also select random windows and calculate the
# similarity between the chosen window and *all* other windows.

import sys

for line in sys.stdin:
    pass
