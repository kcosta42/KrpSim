import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument("-f", "--file", type=str, default=None, required=True)
  parser.add_argument("-r", "--result", type=str, default=None, required=True)

  args = parser.parse_args()
