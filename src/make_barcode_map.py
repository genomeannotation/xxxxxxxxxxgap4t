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

WINDOW_SIZE = 10000

windows = {} # a dictionary that maps window number to a list of barcodes

all_barcodes = set()
for line in sys.stdin:
    fields = line.strip().split()
    seq_id = fields[2]
    position = int(fields[3])
    for field in reversed(fields):
        if field.startswith("RX"):
            barcode_field = field
    barcode = barcode_field.split(":")[2]
    window_number = int(position / WINDOW_SIZE + 1)
    all_barcodes.add(barcode)
    if window_number in windows:
        windows[window_number].add(barcode)
    else:
        windows[window_number] = set([barcode])

# Build barcode map

barcode_map = {}
for i, barcode in enumerate(all_barcodes):
    barcode_map[barcode] = i
    sys.stdout.write(barcode+"\n")

# Output

for window, barcodes in windows.items():
    sys.stdout.write(">"+str(window)+"\n")
    for barcode in barcodes:
        sys.stdout.write(str(barcode_map[barcode])+"\n")
