import sys
import os
import argparse

#handle command line arugments
parser = argparse.ArgumentParser()

parser.add_argument("-min", "--min", help="Minimum line count", required=True)
parser.add_argument("-max", "--max", help="Maximum line count", required=True)
parser.add_argument("-u", "--unsafe", help="Delete without checking", required=False)

#loop through current directory and delete files that are not in the line count range
cwd = os.getcwd()
filePaths = []
for root, dirs, files in os.walk(cwd):
    for file in files:
        try:
            file_path = os.path.join(root, file)
            file_lines = sum(1 for line in open(file_path))
            if file_lines < int(parser.max) and file_lines > int(parser.min):
                filePaths.append(file_path)
        except:
            pass

if parser.unsafe:
    for file in filePaths:
        os.remove(file)
else:
    for file in filePaths:
        print(file)
    a = input("\nType yes if all of these files can be removed else type no")
    if 'y' in a.lower():
        for file in filePaths:
            os.remove(file)
    else:
        print("\nExiting")
        sys.exit()
    