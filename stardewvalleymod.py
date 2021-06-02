import argparse
from argparse import RawTextHelpFormatter
import re

def main(args):
  filename = args.savefile

  with open(filename, 'r') as fin:
    filestring = fin.read()

  newdata = re.sub(r'<money>\d*', r'<money>' + str(args.money), filestring)

  with open(filename, 'w') as fout:
    fout.write(newdata)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
  parser.add_argument("--savefile", required=True, help='Path location of save file (i.e. Replace Farm_123456789 with your save name,'
    '\n Windows: "%%AppData%%\StardewValley\Saves\Farm_123456789\Farm_123456789",' 
    '\n Mac:     "~/.config/StardewValley/Saves/Farm_123456789/Farm_123456789")')
  parser.add_argument("--money", default=99999999, help='Amount of money to set, default: 99999999')
  args = parser.parse_args()
  main(args)
