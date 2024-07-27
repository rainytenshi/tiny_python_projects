#!/home/kunatenshi/miniconda3/bin/python3
#Purpose: Say Hello

import argparse
parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')




print('Hello, World!')
