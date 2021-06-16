import argparse
from argparse import RawTextHelpFormatter
import os
import re
from distutils.dir_util import copy_tree

def main(args):
  filepath = args.savefile
  savedir = os.path.dirname(filepath)
  savename = os.path.basename(filepath)
  savepath = os.path.join(savedir, 'SaveGameInfo')

  # Copy save directory
  if (args.copy_save):
    savesdir = os.path.dirname(os.path.dirname(savedir))
    copynum = 1
    copydir = os.path.join(savesdir, savename + '-' + str(copynum))
    while os.path.exists(copydir):
      copynum += 1
      copydir = copydir[:-2]
      copydir += '-' + str(copynum)
    copy_tree(savedir, copydir)

  # Read game file, save file
  with open(filepath, 'r') as fin:
    newdata = fin.read()
  with open(savepath, 'r') as fin:
    savedata = fin.read()

  # Modify data
  if args.money:
    newdata = re.sub(r'<money>\d*', r'<money>' + str(args.money), newdata)
    savedata = re.sub(r'<money>\d*', r'<money>' + str(args.money), savedata)

  # Overwrite game file, save file
  with open(filepath, 'w') as fout:
    fout.write(newdata)
  with open(savepath, 'w') as fout:
    fout.write(savedata)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
  parser.add_argument('--savefile', required=True, help='Path location of save directory.'
    '\n (i.e. Replace Farm_123456789 with your save name,'
    '\n Windows: "%%AppData%%\StardewValley\Saves\Farm_123456789\Farm_123456789",' 
    '\n Mac:     "~/.config/StardewValley/Saves/Farm_123456789\Farm_123456789")')
  parser.add_argument('--copy_save', action='store_true', help='Create a copy of the save before modifying.'
    '\n It is recommended to copy original save at least once.'
    '\n Note: this will keep adding new copies even when previous copies exist.')
  parser.add_argument('--money', type=int, help='Amount of money to set')
  # TODO Add friendship value mods
  # TODO Add items
  # TODO Change year, season, day
  # TODO Change relationship status
  # TODO Change animal name
  # TODO Change player name
  args = parser.parse_args()
  main(args)
