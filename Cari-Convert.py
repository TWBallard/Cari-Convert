#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Simple Python Console App To Convert Some Values")
parser.add_argument('Quantity', default="1", help="The Number of Source Units")
parser.add_argument('SourceUnit', default="Meter", help="The Source Unit")
parser.add_argument('TargetUnit', default="Kilometer", help="The Target Units")

def main():
    args = parser.parse_args()

    print(f'{args.Quantity}  {args.SourceUnit}  is x many {args.TargetUnit}')



main()
