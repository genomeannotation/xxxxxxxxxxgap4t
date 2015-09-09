#!/usr/bin/env python

# this script will read a sample sam file from stdin 
# and calculate the "similarity" between
# adjacent windows of the sequence, based on barcodes associated with loci.
# it's meant to help with sketching out a reasonable "similarity" metric and 
# to help characterize the data so we know what to expect.

# toward this latter end, it'll also select random windows and calculate the
# similarity between the chosen window and *all* other windows.

import sys
import random

WINDOW_SIZE = 500

windows = {} # a dictionary that maps window number to a list of barcodes

for line in sys.stdin:
    fields = line.strip().split()
    seq_id = fields[2]
    position = int(fields[3])
    for field in reversed(fields):
        if field.startswith("RX"):
            barcode_field = field
    barcode = barcode_field.split(":")[2]
    window_number = int(position / WINDOW_SIZE + 1)
    if window_number in windows:
        windows[window_number].add(barcode)
    else:
        windows[window_number] = set([barcode])

# Print similarity scores between randomly chosen window and all others
all_keys = sorted(windows.keys())
random_window = random.choice(all_keys)
random_window_barcodes = windows[random_window]
print("similarity between window %i and all others: " % random_window)
for window, barcode_list in windows.items():
    sys.stderr.write(str(window))
    sys.stderr.write(": ")
    sys.stderr.write(str(len(random_window_barcodes & barcode_list)) + "\n")


