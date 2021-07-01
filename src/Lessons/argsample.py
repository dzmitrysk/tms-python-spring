import argparse
import sys
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('echo')
parser.add_argument('echo2')
parser.add_argument('echo3')
args = parser.parse_args()


print(args)
print('First name:', args.first_name)
print('Last name:', args.last_name)
print('echo:', args.echo)
print('echo:', args.echo2)
print('echo:', args.echo3)
