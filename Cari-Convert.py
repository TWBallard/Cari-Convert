#!/usr/bin/env python3

import argparse
import csv

parser = argparse.ArgumentParser(description="Simple Python Console App To Convert Some Values")
parser.add_argument('Quantity', default="1", help="The Number of Source Units")
parser.add_argument('SourceUnit', default="Meter", help="The Source Unit")
parser.add_argument('TargetUnit', default="Kilometer", help="The Target Units")
parser.add_argument('--db', default="units.csv", help="The file containing the Database")

def main():
    args = parser.parse_args()
    db = csv.DictReader(open(args.db))

    #Perform Conversion
    x = convert(args.Quantity, args.SourceUnit, args.TargetUnit, db)

    #Output Conversion
    print(f'{args.Quantity}  {args.SourceUnit}  is {x} many {args.TargetUnit}')

def convert(Quantity, SourceUnit, TargetUnit, db):

    x = "42"

    return(x)



main()
