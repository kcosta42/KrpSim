import argparse

from sources.core import main

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument("file", type=str, default=None)
  parser.add_argument("delay", type=int, default=10)

  args = parser.parse_args()

  main(args)
