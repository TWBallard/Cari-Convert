#!/usr/bin/env python3

import argparse
import pandas as pandaReader

parser = argparse.ArgumentParser(description="Simple Python Console App To Convert Some Values")
parser.add_argument('Quantity', default="1", help="The Number of Source Units")
parser.add_argument('SourceUnit', default="Meter", help="The Source Unit")
parser.add_argument('TargetUnit', default="Kilometer", help="The Target Units")
parser.add_argument('--db', default="units.csv", help="The file containing the Database")

def main():
    args = parser.parse_args()

    #Read DB to return Factor
    factor = readdb(args.SourceUnit, args.TargetUnit, args.db)
    #print(f'factor is {factor}')

    #Perform Conversion
    x = convert(args.Quantity, factor)

    #Output Conversion
    print(f'{args.Quantity}  {args.SourceUnit}  is {x} {args.TargetUnit}')

def readdb(SourceUnit, TargetUnit, dbPath):
    db = pandaReader.read_csv(dbPath)
    #print(f'output: {db.iloc[0].SourceUnit}')
    for index, row in db.iterrows():
        if row.SourceUnit == SourceUnit and row.TargetUnit == TargetUnit:
            return(row.Factor)
        if row.SourceUnit == TargetUnit and row.TargetUnit == SourceUnit:
            return(1.0/float(row.Factor))

def convert(quantity, factor):
    return(float(quantity) * float(factor))
main()
