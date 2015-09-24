#!/usr/bin/env python

# Read a sam file with barcoded reads. For each seq/chromosome
# represented in the file, store a list of barcodes found on it
# and a count of how many times it appears

import sys

def main():
    seqs = {} # a dictionary that maps seq_id to a list of barcodes

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
        if window_number in seqs:
            seqs[window_number].add(barcode)
        else:
            seqs[window_number] = set([barcode])

    # Build barcode map

    barcode_map = {}
    for i, barcode in enumerate(all_barcodes):
        barcode_map[barcode] = i
        sys.stdout.write(barcode+"\n")

    # Output

    for window, barcodes in seqs.items():
        sys.stdout.write(">"+str(window)+"\n")
        for barcode in barcodes:
            sys.stdout.write(str(barcode_map[barcode])+"\n")

if __name__ == "__main__:
    main()
