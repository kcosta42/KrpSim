class Simulation(object):
  def __init__(self):
    self.stocks = {}
    self.processes = []
    self.optimizing = []

  def stock(self, name, quantity):
    if name in self.stocks:
      self.stocks[name] += quantity
    else:
      self.stocks[name] = quantity
    return self

  def process(self, process):
    self.processes.append(process)
    return self

  def optimize(self, name):
    self.optimizing.append(name)
    return self
