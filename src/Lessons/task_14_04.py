import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-fn", '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
args = parser.parse_args()


with open('result.txt', 'w') as f:
    f.write(' '.join([args.first_name, args.last_name]))

