import re

from sources.process import Process
from sources.simulation import Simulation

def main(args):
  with open(args.file, 'r') as file:
    raw = [re.sub('#.*', '', line.strip()) for line in file]
    print(raw)
