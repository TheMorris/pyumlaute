"""Receives path to file(s) and replaces 'ae', 'oe', 'ue' with german umlauts"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="path to file")
args = parser.parse_args()


with open("test.txt", "r+") as newdoc:
    backup = newdoc.readlines()
    with open("test_original.txt", 'w+') as original:
        original.writelines(backup)
        original.truncate()
        newdoc.seek(0)
        original.seek(0)
        orlines = original.readlines()
        for line in orlines:
            newdoc.write(line.replace("ae", "ä"))